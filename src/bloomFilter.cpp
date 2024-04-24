#include "bloomFilter.h"
#include "MurmurHash3.h"
#include <stdio.h>
#include <iostream>
#include <cstring>
#include <stdexcept>

#include <openssl/md5.h>

BloomFilter::BloomFilter(uint64_t filterSize, bool useMD5 = false){
    //Save the size of the BloomFilter
    this->filterSize = filterSize;
    //Initialize the BloomFilter with all false
    this->filterMask.assign(filterSize, false);
    //Save the hashing algorithm decision
    this->useMD5 = useMD5;
}

std::array<uint64_t, 2> BloomFilter::hashMD5(const unsigned char* buf, uint32_t len){
    unsigned char md5Hash[MD5_HASH_SIZE];
    std::array<uint64_t, 2> result;

    //Hash data using the MD5 algorithm
    MD5(buf, len, md5Hash);

    //Convert the 16 byte MD5 digest to 2 different 8 byte integers
    std::memcpy(&result[0], &md5Hash[0], sizeof(uint64_t));
    std::memcpy(&result[1], &md5Hash[8], sizeof(uint64_t));

    return result;
}

std::array<uint64_t, 2> BloomFilter::hashMurmur3(const unsigned char* buf, uint32_t len){
    std::array<uint64_t, 2> result;

    //Hash data using the MurmurHash3 algorithm
    MurmurHash3_x64_128(buf, len, 0, result.data());

    return result;
}

std::array<uint64_t, 2> BloomFilter::hash(const unsigned char* buf, uint32_t len) {

    //Execute the desired hashing algorithm
    if (useMD5) {
        return hashMD5(buf, len);
    }

    return hashMurmur3(buf, len);

}

uint64_t BloomFilter::mixHashes(uint32_t n, std::array<uint64_t, 2> hashes){
    //Mix 2 hashes in order to produce an arbitrary number of valid filter positions
	return (hashes[0] + n * hashes[1]) % filterSize;
}

bool BloomFilter::getMaskAt(uint64_t position){
    //Return the status of the mask at given location.
    //Throws an execption when trying to access out of bound data.
    if(position < filterSize){
        return filterMask[position];
    }

    throw std::runtime_error("Position out of bounds");
}

void BloomFilter::addFilter(const unsigned char* buf, uint32_t len){
    //Compute the hashes of a given char array and set the corresponding locations
    //in the filter mask
	auto hashes = hash(buf, len);
	for (int i = 0; i < NUM_HASHES; i++) {
        filterMask[mixHashes(i, hashes)] = true;
	}
}

bool BloomFilter::isProbablyPresent(const unsigned char* buf, uint32_t len){
    //Check if the given element is probably present in the filter.
    //Do this by computing its hashes and checking the relative filter mask
    //locations.
	auto hashes = hash(buf, len);
	for (int i = 0; i < NUM_HASHES; i++) {
		if(!filterMask[mixHashes(i, hashes)]) {
			return false;
		}
	}
	return true;
}

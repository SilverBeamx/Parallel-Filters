#ifndef BLOOMFILTER_H
#define BLOOMFILTER_H

#include <cstdint>
#include <vector>
#include <array>

const uint32_t MD5_HASH_SIZE = 16;
const uint32_t NUM_HASHES = 2;

class BloomFilter {

    private:
        bool useMD5;
        uint64_t filterSize;
        std::vector<bool> filterMask;

    public:
        BloomFilter(uint64_t filterSize, bool useMD5);
        std::array<uint64_t, 2> hashMD5(const unsigned char* buf, uint32_t len);
        std::array<uint64_t, 2> hashMurmur3(const unsigned char* buf, uint32_t len);
        std::array<uint64_t, 2> hash(const unsigned char* buf, uint32_t len);
        uint64_t mixHashes(uint32_t n, std::array<uint64_t, 2> hashes);
        bool getMaskAt(uint64_t position);
        void addFilter(const unsigned char* buf, uint32_t len);
        bool isProbablyPresent(const unsigned char* buf, uint32_t len);
    
};

#endif
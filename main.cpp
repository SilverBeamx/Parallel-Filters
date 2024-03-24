#include "bloomFilter.h"

#include <iostream>


const char* boolAsString(bool src){
    if(src){
        return "true";
    }
    return "false";
}


void testBloom(){

    BloomFilter* bf = new BloomFilter(1234);
    const unsigned char* test = (unsigned char*)"test";
    auto result = bf->hashMD5(test,4);
    std::cout << "Hashes: " << result[0] << " | " << result[1] << std::endl;

    uint64_t hash0 = bf->mixHashes(0,result);
    uint64_t hash1 = bf->mixHashes(1,result);
    std::cout << "Mix 0 Result: " << hash0 << std::endl;
    std::cout << "Mix 1 Result: " << hash1 << std::endl;

    std::cout << "Filter before: " << boolAsString(bf->getMaskAt(hash0)) << " ";
    std::cout << boolAsString(bf->getMaskAt(hash1)) << std::endl;

    bf->addFilter(test, 4);

    std::cout << "Filter after: " << boolAsString(bf->getMaskAt(hash0)) << " ";
    std::cout << boolAsString(bf->getMaskAt(hash1)) << std::endl;

    const unsigned char* arnoldo = (unsigned char*)"Arnoldo";
    std::cout << "Test presence of \"Arnoldo\": ";
    std::cout << boolAsString(bf->isProbablyPresent(arnoldo, 8)) << std::endl;
    std::cout << "Test presence of \"test\": ";
    std::cout << boolAsString(bf->isProbablyPresent(test, 4)) << std::endl;

}

int main(){

    testBloom();

    return 0;
}
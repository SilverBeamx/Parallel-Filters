#ifndef CPUBLOOM_H
#define CPUBLOOM_H

#include "bloomFilter.h"

#include <string>
#include <vector>

class ThreadedBloom{

    private:
        BloomFilter* bf;
        uint32_t numThreads;

    public:
        ThreadedBloom(uint64_t filterSize, uint32_t numThreads, bool useMD5);
        ~ThreadedBloom();
        void addFilter(const unsigned char* buf, uint32_t len);
        std::vector<bool> isProbablyPresent(std::vector<std::string>& wordList);
        void dispatchWork(std::vector<std::string>&, uint32_t, uint32_t, uint32_t, std::vector<bool>&);

};

#endif
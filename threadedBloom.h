#ifndef CPUBLOOM_H
#define CPUBLOOM_H

#include "bloomFilter.h"

#include <vector>

class ThreadedBloom{

    private:
        BloomFilter* bf;
        uint32_t numThreads;

    public:
        ThreadedBloom(uint64_t filterSize, uint32_t numThreads);
        ~ThreadedBloom();
        void addFilter(const unsigned char* buf, uint32_t len);
        std::vector<bool> isProbablyPresent(std::vector<const char*> wordList);
        void dispatchWork(std::vector<const char*>, uint32_t, uint32_t, std::vector<bool>&);

};

#endif
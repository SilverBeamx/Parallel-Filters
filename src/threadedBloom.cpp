#include "threadedBloom.h"

#include <cstring>
#include <iostream>
#include <thread>
#include <future>

ThreadedBloom::ThreadedBloom(uint64_t filterSize, uint32_t numThreads){
    this->bf = new BloomFilter(filterSize);
    this->numThreads = numThreads;
}

ThreadedBloom::~ThreadedBloom(){
    delete this->bf;
}

void ThreadedBloom::addFilter(const unsigned char* buf, uint32_t len){
    bf->addFilter(buf, len);
}

void ThreadedBloom::dispatchWork(std::vector<std::string>& wordList, uint32_t startingIndex, 
                                 uint32_t workSize, std::vector<bool>& result){

    for(uint32_t i = 0; i < workSize; i++){
        uint32_t workIndex = startingIndex+i;
        const unsigned char* word = (unsigned char*)wordList[workIndex].c_str();
        result[workIndex] = bf->isProbablyPresent(word, strlen(wordList[workIndex].c_str()));
    }

}

std::vector<bool> ThreadedBloom::isProbablyPresent(std::vector<std::string>& wordList){

    std::thread threadList[numThreads];
    uint32_t threadWorkAmount = wordList.size() / numThreads;
    int leftoverWork = wordList.size() % numThreads;
    uint32_t startingIndex = 0;
    std::vector<bool> result(wordList.size(), false);

    for (int i = 0; i < numThreads; i++) {
        uint32_t workSize = threadWorkAmount + (leftoverWork-- > 0 ? 1 : 0);
        threadList[i] = std::thread(&ThreadedBloom::dispatchWork, this, std::ref(wordList), startingIndex, workSize, std::ref(result));
        startingIndex += workSize;
    }

    for (int i = 0; i < numThreads; i++) {
        threadList[i].join();
    }

    return result;

}

#include "threadedBloom.h"

#include <iostream>
#include <vector>

int main(){
    std::vector<std::string> testList{"this", "that", "thot", "test"};
    ThreadedBloom* tb = new ThreadedBloom(1234, 3);

    tb->addFilter((unsigned char*)"test", 4);
    auto result = tb->isProbablyPresent(testList);

    for (int i = 0; i < result.size(); ++i){
        std::cout << result[i] << ' ';
    }
    std::cout << std::endl;

    return 0;

}
#include "threadedBloom.h"
#include "utils.h"

#include <chrono>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

int main(){
    using std::chrono::high_resolution_clock;
    using std::chrono::duration_cast;
    using std::chrono::duration;
    using std::chrono::milliseconds;
    using std::chrono::microseconds;

    std::vector<std::string> lineVector;
    readFileByLine("./generate_input_script/fruitList.txt", lineVector);

    auto t1 = high_resolution_clock::now();

    ThreadedBloom* tb = new ThreadedBloom(1234, 12);

    tb->addFilter((unsigned char*)"test", 4);

    auto result = tb->isProbablyPresent(lineVector);
    auto t2 = high_resolution_clock::now();
    auto time_elapsed = duration_cast<microseconds>(t2 - t1);

    std::cout << "Elapsed filter find time: " << time_elapsed.count() << " us" << std::endl;

    return 0;

}
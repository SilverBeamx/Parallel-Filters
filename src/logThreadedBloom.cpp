#include "threadedBloom.h"
#include "utils.h"

#include "args.h"

#include <chrono>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace args;

int main(int argc, char **argv){
    using std::chrono::high_resolution_clock;
    using std::chrono::duration_cast;
    using std::chrono::duration;
    using std::chrono::milliseconds;
    using std::chrono::microseconds;

    ArgParser cmd_parser("Usage: -n/--numThreads [NUM_THREADS]\n-l/--log Log to output.txt", "1.0");

    cmd_parser.flag("log l");
    cmd_parser.option("numThreads n", "20");
    cmd_parser.parse(argc, argv);

    uint32_t numThreads = std::stoi(cmd_parser.value("numThreads"));

    std::vector<std::string> lineVector;
    readFileByLine("./generate_input_script/fruitList.txt", lineVector);

    auto t1 = high_resolution_clock::now();

    ThreadedBloom* tb = new ThreadedBloom(1234, numThreads);

    tb->addFilter((unsigned char*)"test", 4);

    auto result = tb->isProbablyPresent(lineVector);
    auto t2 = high_resolution_clock::now();
    auto time_elapsed = duration_cast<microseconds>(t2 - t1);

    std::cout << "Elapsed filter find timeee: " << time_elapsed.count() << " us" << std::endl;

    if(cmd_parser.found("log")){
        std::ofstream output("log/threadedTiming.txt", std::ios_base::app);
        output << numThreads << "," << time_elapsed.count() << std::endl;
    }

    return 0;

}
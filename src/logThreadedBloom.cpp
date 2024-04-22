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
    using std::chrono::steady_clock;
    using std::chrono::duration_cast;
    using std::chrono::duration;
    using std::chrono::milliseconds;
    using std::chrono::microseconds;

    std::cout << "Parsing args" << std::endl;

    ArgParser cmd_parser("Usage: -n/--numThreads [NUM_THREADS]\n-l/--log Log to output.txt", "1.0");

    cmd_parser.flag("log l");
    cmd_parser.option("numThreads n", "20");
    cmd_parser.parse(argc, argv);

    uint32_t numThreads = std::stoi(cmd_parser.value("numThreads"));
    std::cout << "Loading dataset" << std::endl;

    std::vector<std::string> lineVector;
    readFileByLine("./scripts/fruitList.txt", lineVector);
    std::cout << "Dataset loaded: " << lineVector.size() << " words loaded" << std::endl;

    auto t1 = steady_clock::now();

    ThreadedBloom* tb = new ThreadedBloom(1234, numThreads, false);

    tb->addFilter((unsigned char*)"test", 4);

    auto result = tb->isProbablyPresent(lineVector);
    auto t2 = steady_clock::now();
    auto time_elapsed = duration_cast<microseconds>(t2 - t1);

    std::cout << "Elapsed filter find time: " << time_elapsed.count() << " us" << std::endl;

    if(cmd_parser.found("log")){
        std::ofstream output("log/threadedTiming.csv", std::ios_base::app);
        output << lineVector.size() << "," << numThreads << "," << time_elapsed.count() << std::endl;
    }

    return 0;

}
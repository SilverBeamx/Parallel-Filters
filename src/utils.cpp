#include <fstream>
#include <string>
#include <vector>

#include <iostream>

void readFileByLine(std::string fileName, std::vector<std::string>& lineVector){

    std::ifstream file(fileName);
    std::string line;

    while (std::getline(file, line)){
        lineVector.push_back(line);
    }
}
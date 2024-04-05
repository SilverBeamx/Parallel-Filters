CXXFLAGS = -Wall -Wextra -Wno-unused-parameter --std=c++11

bloomFilter.o: bloomFilter.cpp bloomFilter.h
	g++ -c bloomFilter.cpp

threadedBloom.o: bloomFilter.o threadedBloom.cpp threadedBloom.h
	g++ -c threadedBloom.cpp

utils.o: utils.cpp utils.h
	g++ -c utils.cpp

args.o:
	$(CXX) $(CXXFLAGS) -c -o args.o argspp/src/args.cpp

testBloomFilter.exe: bloomFilter.o testBloomFilter.cpp
	g++ -o testBloomFilter.exe bloomFilter.o testBloomFilter.cpp -lcrypto

testBloom: testBloomFilter.exe
	./testBloomFilter.exe

testThreadedBloom.exe: threadedBloom.o testThreadedBloom.cpp
	g++ -o testThreadedBloom.exe bloomFilter.o threadedBloom.o testThreadedBloom.cpp -lcrypto

testThreadedBloom: testThreadedBloom.exe
	./testThreadedBloom.exe

testThreadedBloomTiming.exe: threadedBloom.o utils.o testThreadedBloomTiming.cpp
	g++ -o testThreadedBloomTiming.exe bloomFilter.o threadedBloom.o utils.o testThreadedBloomTiming.cpp -lcrypto

testThreadedBloomTiming: testThreadedBloomTiming.exe
	./testThreadedBloomTiming.exe

logThreadedBloom.exe: threadedBloom.o utils.o args.o logThreadedBloom.cpp
	g++ -o logThreadedBloom.exe bloomFilter.o threadedBloom.o utils.o args.o logThreadedBloom.cpp -lcrypto

testThreadedTimingArguments: logThreadedBloom.exe
	./logThreadedBloom.exe

testThreadedLog: logThreadedBloom.exe
	./logThreadedBloom.exe -n 12 -l
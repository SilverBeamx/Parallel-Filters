bloomFilter.o: bloomFilter.cpp bloomFilter.h
	g++ -c bloomFilter.cpp

threadedBloom.o: bloomFilter.o threadedBloom.cpp threadedBloom.h
	g++ -c threadedBloom.cpp

buildTestBloomFilter: bloomFilter.o testBloomFilter.cpp
	g++ -o testBloomFilter bloomFilter.o testBloomFilter.cpp -lcrypto

testBloom: buildTestBloomFilter
	./testBloomFilter

buildTestThreadedBloom: threadedBloom.o testThreadedBloom.cpp
	g++ -o testThreadedBloom bloomFilter.o threadedBloom.o testThreadedBloom.cpp -lcrypto

testThreadedBloom: buildTestThreadedBloom
	./testThreadedBloom

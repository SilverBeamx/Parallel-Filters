bloomFilter: bloomFilter.cpp main.cpp
	g++ -o bloomFilter bloomFilter.cpp main.cpp -lcrypto

run: bloomFilter
	./bloomFilter
BIN_PATH := bin
OBJ_PATH := obj
SRC_PATH := src
TEST_PATH := test
INC_PATH := $(SRC_PATH)/include

CFLAGS = -I$(INC_PATH) -lcrypto 
CXXOBJFLAGS = -c

MAIN_FILE := logThreadedBloom

SRC := $(foreach x, $(SRC_PATH), $(wildcard $(addprefix $(x)/*,.c*)))
OBJS := $(addprefix $(OBJ_PATH)/, $(addsuffix .o, $(notdir $(basename $(SRC)))))
NON_MAIN_OBJS := $(filter-out $(OBJ_PATH)/$(MAIN_FILE).o, $(OBJS))

run: $(BIN_PATH)/threadedBloom.exe
	./$(BIN_PATH)/threadedBloom.exe -l

$(BIN_PATH)/threadedBloom.exe: $(OBJS)
	$(CXX) -o $(BIN_PATH)/threadedBloom.exe $(OBJS) $(CFLAGS)

$(OBJ_PATH)/%.o: $(SRC_PATH)/%.c*
	$(CXX) $(CXXOBJFLAGS) -o $@ $<

$(BIN_PATH)/testBloomFilter.exe: $(NON_MAIN_OBJS) $(TEST_PATH)/testBloomFilter.cpp
	$(CXX) -o $(BIN_PATH)/testBloomFilter.exe $(TEST_PATH)/testBloomFilter.cpp $(NON_MAIN_OBJS) $(CFLAGS)

testBloom: $(BIN_PATH)/testBloomFilter.exe
	./$(BIN_PATH)/testBloomFilter.exe

$(BIN_PATH)/testThreadedBloom.exe: $(NON_MAIN_OBJS) $(TEST_PATH)/testThreadedBloom.cpp
	$(CXX) -o $(BIN_PATH)/testThreadedBloom.exe $(TEST_PATH)/testThreadedBloom.cpp $(NON_MAIN_OBJS) $(CFLAGS)

testThreadedBloom: $(BIN_PATH)/testThreadedBloom.exe
	./$(BIN_PATH)/testThreadedBloom.exe

$(BIN_PATH)/testThreadedBloomTiming.exe: $(NON_MAIN_OBJS) $(TEST_PATH)/testThreadedBloomTiming.cpp
	$(CXX) -o $(BIN_PATH)/testThreadedBloomTiming.exe $(TEST_PATH)/testThreadedBloomTiming.cpp $(NON_MAIN_OBJS) $(CFLAGS)

testThreadedBloomTiming: $(BIN_PATH)/testThreadedBloomTiming.exe
	./$(BIN_PATH)/testThreadedBloomTiming.exe
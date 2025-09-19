# --- Compiler and Flags ---
CXX := C:/msys64/ucrt64/bin/g++.exe
CXXFLAGS := -O2 -std=c++20 -g -Wall -IC:/msys64/ucrt64/include
# Add the -static-libgcc flag to this line
LDFLAGS := -LC:/msys64/ucrt64/lib -ljsoncpp -static-libstdc++ -static-libgcc

# --- Project Structure ---
BUILD_DIR := build
TEST_RUNNER_SRC := tests_runner/tests_runner.cpp

# --- Auto-discovery of Problems ---
PROBLEM_DIRS := $(wildcard problems/problem_*)
PROBLEM_NUMS := $(patsubst problems/problem_%,%,$(PROBLEM_DIRS))

# --- Main Targets ---
.PHONY: test-all
test-all: $(addprefix test-, $(PROBLEM_NUMS))
	@echo ""
	@echo "✅ All tests completed."

.PHONY: test-%
test-%: $(BUILD_DIR)/problem_%/runner.exe
	@echo "--- Running tests for Problem $* ---"
	@$(BUILD_DIR)/problem_$*/runner.exe -f problems/problem_$*/problem_$*.json

# --- Build Rules ---
$(BUILD_DIR)/problem_%/runner.exe: $(TEST_RUNNER_SRC) problems/problem_%/solution.cpp
	@mkdir -p $(@D)
	$(CXX) $(CXXFLAGS) -Iproblems/problem_$* -Itests_runner $^ -o $@ $(LDFLAGS)

# --- Utility Targets ---
.PHONY: clean
clean:
	@echo "Cleaning build directory..."
	@rm -rf $(BUILD_DIR)
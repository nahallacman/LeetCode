#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <stdexcept>

// This is the only external library header we need
#include <json/json.h>

// Include the solution file for the problem being tested
#include "solution.hpp"

// --- Simple ANSI Color Codes for Terminal Output ---
const char* const RESET_COLOR = "\033[0m";
const char* const GREEN_COLOR = "\033[32m";
const char* const RED_COLOR   = "\033[31m";
const char* const BOLD_WHITE  = "\033[1m\033[37m";

// --- Helper function to parse stringified vectors like "[1,2,3]" ---
std::vector<int> parse_int_vector_string(const std::string& s) {
    std::string content = s.substr(1, s.length() - 2); // Remove brackets
    if (content.empty()) {
        return {};
    }
    std::vector<int> vec;
    std::stringstream ss(content);
    std::string item;
    while (std::getline(ss, item, ',')) {
        vec.push_back(std::stoi(item));
    }
    return vec;
}

// --- Main Test Runner Logic ---
int main(int argc, char* argv[]) {
    // 1. Parse Command-Line Arguments for the JSON file path
    std::string json_path;
    for (int i = 1; i < argc; ++i) {
        std::string arg = argv[i];
        if (arg == "-f" && i + 1 < argc) {
            json_path = argv[++i];
        }
    }

    if (json_path.empty()) {
        std::cerr << RED_COLOR << "Error: No JSON test file provided. Usage: -f <path>" << RESET_COLOR << std::endl;
        return 1;
    }

    // 2. Read and Parse the JSON file
    std::ifstream ifs(json_path);
    if (!ifs.is_open()) {
        std::cerr << RED_COLOR << "Error: Could not open file: " << json_path << RESET_COLOR << std::endl;
        return 1;
    }

    Json::Value root;
    try {
        ifs >> root;
    } catch (const std::exception& e) {
        std::cerr << RED_COLOR << "Error: Failed to parse JSON file: " << e.what() << RESET_COLOR << std::endl;
        return 1;
    }
    
    // 3. Execute Tests
    std::string method_name = root["method"].asString();
    const Json::Value& tests = root["tests"];
    
    std::cout << BOLD_WHITE << "Running tests for method: " << method_name << RESET_COLOR << std::endl;
    std::cout << "------------------------------------------" << std::endl;

    Solution solution;
    int tests_passed = 0;
    int total_tests = tests.size();

    for (int i = 0; i < total_tests; ++i) {
        const auto& test = tests[i];
        std::cout << "Test Case #" << (i + 1) << "... ";

        try {
            if (method_name == "twoSum") {
                // Parse inputs and expected output
                auto nums = parse_int_vector_string(test["Input"]["nums"].asString());
                int target = std::stoi(test["Input"]["target"].asString());
                auto expected = parse_int_vector_string(test["Output"].asString());

                // Run the actual function
                auto actual = solution.twoSum(nums, target);

                // Sort both vectors to handle different ordering (e.g., [0,1] vs [1,0])
                std::sort(expected.begin(), expected.end());
                std::sort(actual.begin(), actual.end());

                // Assert and report
                if (actual == expected) {
                    std::cout << GREEN_COLOR << "PASS" << RESET_COLOR << std::endl;
                    tests_passed++;
                } else {
                    std::cout << RED_COLOR << "FAIL" << RESET_COLOR << std::endl;
                    // You can add more detailed failure output here if you want
                }
            }
            // Add more 'else if' blocks here for other problems
            // else if (method_name == "anotherProblem") { ... }

        } catch (const std::exception& e) {
            std::cout << RED_COLOR << "ERROR: " << e.what() << RESET_COLOR << std::endl;
        }
    }

    // 4. Print Final Summary
    std::cout << "------------------------------------------" << std::endl;
    std::cout << BOLD_WHITE << "Summary: " << tests_passed << " / " << total_tests << " tests passed." << RESET_COLOR << std::endl;

    // Return a non-zero exit code if any tests failed, so 'make' will know
    return (tests_passed == total_tests) ? 0 : 1;
}
#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <stdexcept>
#include <functional>
#include <map>

#include <json/json.h>
#include "solution.hpp"

// --- ANSI Color Codes for Terminal Output ---
const char* const RESET_COLOR = "\033[0m";
const char* const GREEN_COLOR = "\033[32m";
const char* const RED_COLOR   = "\033[31m";
const char* const BOLD_WHITE  = "\033[1m\033[37m";

// --- Generic Helpers for Parsing and Comparing ---
namespace helpers {
    // A set of simple, explicit functions for parsing types from JSON
    int parse_int(const Json::Value& value) {
        return std::stoi(value.asString());
    }

    std::string parse_string(const Json::Value& value) {
        return value.asString();
    }
    
    std::vector<int> parse_int_vector(const Json::Value& value) {
        std::string s = value.asString();
        std::string content = s.substr(1, s.length() - 2);
        if (content.empty()) return {};
        std::vector<int> vec;
        std::stringstream ss(content);
        std::string item;
        while (std::getline(ss, item, ',')) {
            vec.push_back(std::stoi(item));
        }
        return vec;
    }
}

// --- Test Case Handler Framework ---
using TestCaseHandler = std::function<bool(Solution& solution, const Json::Value& test_case)>;
static std::map<std::string, TestCaseHandler> test_registry;

// =======================================================================
// =================== PROBLEM HANDLERS GO HERE ==========================
// =======================================================================

// With helpers, handlers are concise and easy to read.
bool handleTwoSum(Solution& solution, const Json::Value& test) {
    auto nums = helpers::parse_int_vector(test["Input"]["nums"]);
    auto target = helpers::parse_int(test["Input"]["target"]);
    auto expected = helpers::parse_int_vector(test["Output"]);
    
    auto actual = solution.twoSum(nums, target);
    
    // Normalize for comparison, since order doesn't matter for this problem
    std::sort(actual.begin(), actual.end());
    std::sort(expected.begin(), expected.end());

    bool success = (actual == expected);
    
    if(!success) {
        std::cout << std::endl << "actual" << std:: endl;
        for(auto &vals : actual){
            std::cout << vals << " ";
        }
        std::cout << std::endl;
        
        std::cout << "expected:" << std::endl;
        for(auto &vals : expected){
            std::cout << vals << " ";
        }
        std::cout << std::endl;
    }

    return success;
}

// =======================================================================
// =================== REGISTER ALL HANDLERS HERE ========================
// =======================================================================

void register_all_tests() {
    test_registry["twoSum"] = handleTwoSum;
    // To add a new problem, you would add a new handler and register it here.
}

// =======================================================================
// =================== MAIN TEST RUNNER LOGIC ============================
// =======================================================================
int main(int argc, char* argv[]) {
    register_all_tests();

    std::string json_path;
    for (int i = 1; i < argc; ++i) {
        if (std::string(argv[i]) == "-f" && i + 1 < argc) {
            json_path = argv[++i];
        }
    }
    if (json_path.empty()) {
        std::cerr << RED_COLOR << "Error: No JSON test file provided. Usage: -f <path>" << RESET_COLOR << std::endl;
        return 1;
    }

    std::ifstream ifs(json_path);
    if (!ifs.is_open()) {
        std::cerr << RED_COLOR << "Error: Could not open file: " << json_path << RESET_COLOR << std::endl;
        return 1;
    }

    Json::Value root;
    ifs >> root;
    
    std::string method_name = root["method"].asString();
    
    if (test_registry.find(method_name) == test_registry.end()) {
        std::cerr << RED_COLOR << "Error: No test handler registered for method '" << method_name << "'" << RESET_COLOR << std::endl;
        return 1;
    }
    TestCaseHandler handler = test_registry[method_name];

    const Json::Value& tests = root["tests"];
    std::cout << BOLD_WHITE << "Running tests for method: " << method_name << RESET_COLOR << std::endl;
    std::cout << "------------------------------------------" << std::endl;

    Solution solution;
    int tests_passed = 0;
    int total_tests = tests.size();

    for (int i = 0; i < total_tests; ++i) {
        std::cout << "Test Case #" << (i + 1) << "... ";
        try {
            if (handler(solution, tests[i])) {
                std::cout << GREEN_COLOR << "PASS" << RESET_COLOR << std::endl;
                tests_passed++;
            } else {
                std::cout << RED_COLOR << "FAIL" << RESET_COLOR << std::endl;
            }
        } catch (const std::exception& e) {
            std::cout << RED_COLOR << "ERROR: An exception occurred: " << e.what() << RESET_COLOR << std::endl;
        }
    }

    std::cout << "------------------------------------------" << std::endl;
    std::cout << BOLD_WHITE << "Summary: " << tests_passed << " / " << total_tests << " tests passed." << RESET_COLOR << std::endl;

    return (tests_passed == total_tests) ? 0 : 1;
}
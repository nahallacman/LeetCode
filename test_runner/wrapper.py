# In wrapper.py

import json
import sys
import ast
from typing import Type, Any

TEST_PASS_FAIL_PRINT = True

def run_test_cases(Solution: Type, test_input_json: dict) -> bool:
    """
    Runs test cases from a loaded JSON object against a Solution class.
    This version is flexible and handles multiple input/output formats.
    """
    test_passes = []
    test_function_name = test_input_json["method"]

    solver = Solution()

    try:
        method_to_call = getattr(solver, test_function_name)
    except AttributeError:
        print(f"Error: Test method '{test_function_name}' not found in Solution class.")
        return False

    tests = test_input_json["tests"]

    for i, test in enumerate(tests):
        raw_input = test["Input"]
        raw_output = test["Output"]
        actual_output = None
        
        # --- Output Parsing ---
        expected_output = None
        if isinstance(raw_output, str):
            try:
                expected_output = ast.literal_eval(raw_output)
            except (ValueError, SyntaxError):
                expected_output = raw_output
        else:
            expected_output = raw_output

        
        # Case 1: Input is a dictionary of named parameters.
        if isinstance(raw_input, dict):
            parsed_params = {}
            for key, value in raw_input.items():
                # If a value is a string, we TRY to parse it.
                if isinstance(value, str):
                    try:
                        # This works for "[1,2,3]" or "9"
                        parsed_params[key] = ast.literal_eval(value)
                    except (ValueError, SyntaxError):
                        # This works for "Bob hit a ball..."
                        parsed_params[key] = value
                else:
                    # Value is already a number, list, etc. from JSON.
                    parsed_params[key] = value
            actual_output = method_to_call(**parsed_params)
            
        # Case 2: Input is a single value.
        else:
            parsed_input = None
            if isinstance(raw_input, str):
                try:
                    # This works for inputs like "[3,3,3,1,3]"
                    parsed_input = ast.literal_eval(raw_input)
                except (ValueError, SyntaxError):
                    # This works for a simple string input "hello"
                    parsed_input = raw_input
            else:
                # Input is already a number or list from JSON.
                parsed_input = raw_input
            actual_output = method_to_call(parsed_input)

        # --- Comparison ---
        if actual_output == expected_output:
            test_passes.append(True)
        else:
            test_passes.append(False)
            print(f"--- Test #{i+1} FAILED ---")
            print(f"  Input:    {raw_input}")
            print(f"  Expected: {expected_output}")
            print(f"  Actual:   {actual_output}")
            print("------------------------")

    # Process results
    all_passed = True
    for i, passed in enumerate(test_passes):
        if passed:
            if TEST_PASS_FAIL_PRINT:
                print(f"Test #{i+1} PASSED.")
        else:
            if TEST_PASS_FAIL_PRINT:
                print(f"Test #{i+1} FAILED !!!!")
            all_passed = False
            
    return all_passed

def run_tests(Solution, test_input_file_path) -> bool:
    """
    Runs test cases from a JSON file against a solution class.
    """
    print("start")

    # Opening JSON file
    file = open(test_input_file_path)

    # returns JSON object as a dictionary
    test_inputs = json.load(file)

    retval = run_test_cases(Solution, test_inputs)

    if(retval):
        print("All tests passed")
    else:
        print("One or more tests failed")
        sys.exit(1) # <-- Add this line

    print("done")

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

    # Create an instance of the class
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
        
        # --- Flexible Output Parsing (No change here) ---
        expected_output = None
        if isinstance(raw_output, str):
            try:
                expected_output = ast.literal_eval(raw_output)
            except (ValueError, SyntaxError):
                expected_output = raw_output
        else:
            expected_output = raw_output

        # --- Flexible Input Handling & Method Call (UPDATED LOGIC) ---
        # Case 1: Input is a dictionary of named parameters.
        if isinstance(raw_input, dict):
            # The raw_input dictionary's keys match the parameter names.
            # We can unpack it directly into the method call.
            actual_output = method_to_call(**raw_input)
        # Case 2: Input is a single, direct value.
        else:
            actual_output = method_to_call(raw_input)

        # --- Comparison (No change here) ---
        if actual_output == expected_output:
            test_passes.append(True)
        else:
            test_passes.append(False)
            print(f"--- Test #{i+1} FAILED ---")
            print(f"  Input:    {raw_input}")
            print(f"  Expected: {expected_output}")
            print(f"  Actual:   {actual_output}")
            print("------------------------")

    # Process results as in your original script
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

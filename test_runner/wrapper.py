import json
import sys
import ast
from typing import Type, Any
import inspect

TEST_PASS_FAIL_PRINT = True

def run_test_cases(Solution: Type, test_input_json: dict) -> bool:
    """
    Runs test cases from a loaded JSON object against a Solution class.
    This version is flexible and handles multiple input/output formats.
    This version also intelligently inspects function type hints to decide
    whether to parse string inputs or pass them through directly.
    """
    test_passes = []
    test_function_name = test_input_json["method"]

    solver = Solution()

    try:
        method_to_call = getattr(solver, test_function_name)
    except AttributeError:
        print(f"Error: Test method '{test_function_name}' not found in Solution class.")
        return False

    # Get the function signature to inspect its type hints
    try:
        sig = inspect.signature(method_to_call)
    except ValueError:
        # Happens on some built-in types, not expected for user code
        sig = None

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
                expected_type = sig.parameters.get(key).annotation if sig else None
                
                # If the function expects a string and gets a string, pass it directly.
                if isinstance(value, str) and expected_type is str:
                    parsed_params[key] = value
                # Otherwise, check if the value is a string
                elif isinstance(value, str):
                    try:
                        # And attempt to convert it
                        parsed_params[key] = ast.literal_eval(value)
                    except (ValueError, SyntaxError):
                        # If we can't convert it, just use the raw value
                        print("ast.literal_eval() failed, using raw value")
                        parsed_params[key] = value
                else:
                    parsed_params[key] = value
            actual_output = method_to_call(**parsed_params)
            
        # Case 2: Input is a single value.
        else:
            # Get the type hint of the first parameter
            params = list(sig.parameters.values()) if sig else []
            expected_type = params[0].annotation if params else None
            
            parsed_input = None
            # If the function expects a string and gets a string, pass it directly.
            if isinstance(raw_input, str) and expected_type is str:
                parsed_input = raw_input
            # Otherwise, check if the value is a string
            elif isinstance(raw_input, str):
                try:
                    # And attempt to convert it
                    parsed_input = ast.literal_eval(raw_input)
                except (ValueError, SyntaxError):
                    # If we can't convert it, just use the raw value
                    print("ast.literal_eval() failed, using raw value")
                    parsed_input = raw_input
            else:
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

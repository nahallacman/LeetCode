import json
import sys
import ast # Use ast.literal_eval for safely parsing strings
TEST_PASS_FAIL_PRINT = True


def run_test_cases(Solution, test_input_json) -> bool:
    results = []
    test_passes = []
    test_function_name = test_input_json["method"]

    # Create an INSTANCE of the class
    solver = Solution()

    # 3. Use getattr to get the actual method from the solver instance
    try:
        method_to_call = getattr(solver, test_function_name)
    except AttributeError:
        print(f"Error: Test method '{test_function_name}' not found in Solution class.")
        return False
    
    # # Get the array of tests with expected inputs and True/False results
    # tests = test_input_json["tests"]
    # for test in tests:
    #     results.append(method_to_call(test))

    tests = test_input_json["tests"]
    all_passed = True

    for i, test in enumerate(tests):
        raw_params = test["Input"]
        expected_output_str = test["Output"]
        
        # Need two cases here, one for just a literal string and another for a JSON structure of strings that need to be interpreted.
        if isinstance(raw_params, str):
            # Safely parse the expected output as well
            expected_output = ast.literal_eval(expected_output_str)

            # 5. Call the method using ** to unpack the dictionary of parameters
            actual_output = method_to_call(raw_params)
        else:
            # 4. Parse the string inputs into actual Python objects
            parsed_params = {}
            for key, value in raw_params.items():
                # ast.literal_eval safely evaluates a string containing a Python literal
                parsed_params[key] = ast.literal_eval(value)
                
            # Safely parse the expected output as well
            expected_output = ast.literal_eval(expected_output_str)

            # 5. Call the method using ** to unpack the dictionary of parameters
            actual_output = method_to_call(**parsed_params)

        if actual_output == expected_output:
            test_passes.append(True)
        else:
            test_passes.append(False)
    # index = 0
    # for result in results:
    #     expected_result = bool(tests[index]["Result"])
    #     actual_result = bool(test["Result"])
    #     if(expected_result == actual_result):
    #         test_passes.append(True)
    #     index += 1

    index = 0
    for test_pass in test_passes:
        if test_pass == False:
            print(f"Test #{index} did not return the expected result.")
            return False
        elif TEST_PASS_FAIL_PRINT:
            print(f"Test #{index} did return the expected result.")
        index += 1
    return True

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

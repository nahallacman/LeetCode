import json
import sys
TEST_PASS_FAIL_PRINT = True


def run_test_cases(Solution, test_input_json) -> bool:
    results = []
    test_passes = []
    # Get the array of tests with expected inputs and True/False results
    tests = test_input_json["tests"]
    for test in tests:
        results.append(Solution.isValid(test["Input"]))

    index = 0
    for result in results:
        expected_result = bool(tests[index]["Result"])
        actual_result = bool(test["Result"])
        if(expected_result == actual_result):
            test_passes.append(True)
        index += 1

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

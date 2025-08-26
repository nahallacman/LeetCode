import subprocess
from pathlib import Path
import time
import sys
import argparse  # New import for command-line arguments
import xml.etree.ElementTree as ET # New import for XML generation

def main(report_file):
    """
    Finds and runs tests for all 'problem_*' directories.
    """
    project_root = Path(__file__).parent
    problem_folders = sorted([p for p in project_root.iterdir() if p.is_dir() and p.name.startswith("problem_")])
    
    if not problem_folders:
        print("No 'problem_*' folders found to test.")
        return

    print(f"Found {len(problem_folders)} problem folders to test.\n")
    
    start_time = time.time()
    failed_tests = []

    test_results_data = []

    for folder in problem_folders:
        solution_file = folder / "solution.py"
        if solution_file.exists():
            print(f"--- Testing: {folder.name} ---")
            
            test_start_time = time.time()
            # 2. Use sys.executable instead of "python"
            result = subprocess.run(
                [sys.executable, str(solution_file)],
                capture_output=True,
                text=True,
                cwd=project_root
            )
            test_end_time = time.time()

            #Append a dictionary with all of the results for the report generator
            test_results_data.append({
                "name": folder.name,
                "duration": test_end_time - test_start_time,
                "result": result
            })
            
            print(result.stdout)
            if result.stderr:
                print(f"Errors:\n{result.stderr}")

            if result.returncode != 0:
                failed_tests.append(folder.name)
            
        else:
            print(f"--- Skipping: {folder.name} (no solution.py found) ---")

    end_time = time.time()
    
    # --- Final Summary ---
    print("\n======================")
    print("  TEST SUITE SUMMARY  ")
    print("======================")
    print(f"Total time: {end_time - start_time:.2f} seconds")
    print(f"Total problem suites run: {len(problem_folders)}")

    create_report(report_file, test_results_data)
    
    if not failed_tests:
        print("\n✅✅✅ All problem suites passed! ✅✅✅")
    else:
        print(f"\n❌❌❌ {len(failed_tests)} problem suite(s) failed: ❌❌❌")
        for test_name in failed_tests:
            print(f"  - {test_name}")
        exit(1)

def create_report(output_file, test_results):
    print("TODO: generate test report here")
    create_junit_report(output_file, test_results)

def create_junit_report(output_file, test_results):
    """
    NEW: Generates a JUnit XML report from the test results.
    """
    num_tests = len(test_results)
    num_failures = sum(1 for r in test_results if r["result"].returncode != 0)
    total_duration = sum(r["duration"] for r in test_results)

    # Create the root <testsuite> element
    testsuite_attrs = {
        "name": "LeetCode Problems",
        "tests": str(num_tests),
        "failures": str(num_failures),
        "errors": "0",
        "time": f"{total_duration:.3f}",
    }
    testsuite = ET.Element("testsuite", **testsuite_attrs)

    # Create a <testcase> for each result
    for item in test_results:
        result = item["result"]
        
        testcase_attrs = {
            "name": item["name"],
            "classname": "problems", # A grouping name for the test
            "time": f"{item['duration']:.3f}",
        }
        testcase = ET.SubElement(testsuite, "testcase", **testcase_attrs)

        # If the test failed, add a <failure> tag with details
        if result.returncode != 0:
            failure_attrs = {
                "message": f"Test failed with exit code {result.returncode}",
                "type": "TestFailure",
            }
            failure = ET.SubElement(testcase, "failure", **failure_attrs)
            # Add stdout and stderr to the failure message for easy debugging in the UI
            failure_details = f"--- STDOUT ---\n{result.stdout}\n"
            if result.stderr:
                failure_details += f"--- STDERR ---\n{result.stderr}"
            failure.text = failure_details

    # Write the XML tree to the specified file
    tree = ET.ElementTree(testsuite)
    tree.write(output_file, encoding='utf-8', xml_declaration=True)


if __name__ == "__main__":
        # NEW: Use argparse to handle command-line arguments
    parser = argparse.ArgumentParser(description="Run LeetCode tests and generate a report.")
    parser.add_argument(
        "output_file",
        help="The path to the output JUnit XML report file (e.g., test-results.xml)."
    )
    args = parser.parse_args()

    main(args.output_file)

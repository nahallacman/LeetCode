import subprocess
from pathlib import Path
import time
import sys 

def main():
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

    for folder in problem_folders:
        solution_file = folder / "solution.py"
        if solution_file.exists():
            print(f"--- Testing: {folder.name} ---")
            
            # 2. Use sys.executable instead of "python"
            result = subprocess.run(
                [sys.executable, str(solution_file)],
                capture_output=True,
                text=True,
                cwd=project_root
            )
            
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
    
    if not failed_tests:
        print("\n✅✅✅ All problem suites passed! ✅✅✅")
    else:
        print(f"\n❌❌❌ {len(failed_tests)} problem suite(s) failed: ❌❌❌")
        for test_name in failed_tests:
            print(f"  - {test_name}")

if __name__ == "__main__":
    main()

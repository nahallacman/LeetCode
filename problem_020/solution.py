# Extra header to ensure that tests can run individually and as a suite
#  -------------------------------------------------------------------
import sys
from pathlib import Path
# Add the project root folder to the Python path
sys.path.append(str(Path(__file__).resolve().parents[1]))
#  -------------------------------------------------------------------

# Now you can import your wrapper
from test_runner.wrapper import run_tests

class Solution:
    @staticmethod
    def isValid(s: str) -> bool:
        stack = []
        retval = False
        # If there are 1 or 0 characters in the string, there are no matching pairs
        if(len(s) < 2):
            return False
        # Since we know there is at least 2 characters in the string, put the first one into the stack.
        stack.append(s[0])
        # from the 2nd character in the string, iterate and try to see if there is a matching pair.
        for iter in s[1:]:
            # This case breaks things. We are not moving on past 2 successful matches here.
            if not stack:
                stack.append(iter)
                continue
            retval = Solution.close_case(stack[-1], iter)
            # If we successfully found a pair, pop the last value off the stack.
            if(retval):
                stack.pop()
            else:
                # If we don't find a matching closing, but are still trying to close a statement, exit because we found a bad match.
                if(iter == ")" or iter == "}" or iter == "}"):
                    return False
                stack.append(iter)

        if stack:
            return False
        return retval
    
    @staticmethod
    def close_case(last:str, next: str) -> bool:
        if(last == "(" and next == ")"):
            return True
        if(last == "{" and next == "}"):
            return True
        if(last == "[" and next == "]"):
            return True
        return False

if __name__ == "__main__":
    # Get the directory where this solution.py script lives
    script_dir = Path(__file__).parent
    
    # Join the script's directory with the JSON filename to create a full path
    # Make sure your file is actually named "test_inputs.json"!
    test_file_path = script_dir / "test_inputs.json"
    
    run_tests(Solution, test_file_path)
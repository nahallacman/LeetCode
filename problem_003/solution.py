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
    def lengthOfLongestSubstring(self, s: str) -> int:
        # str_start -> str
        hashMap = {}
        measuredLengths = {}
        longest_string = 0
    
        current_string = ""
        last_string = ""
        init = True

        # Iterate over whole string, one character at a time
        for str in s:
            # Initial condition, current_string is empty so put the string into it.
            if not current_string:
                current_string = str
            else:
                if current_string[0] == str:
                    # We are finding a new character string, so we should store the old character string length off somewhere.
                    current_string = current_string[1:] + str
                    measuredLengths[str] = len(hashMap[str])
                else:
                    current_string = current_string + str

            count = 0
            # This is really bad, I know. Fix it.
            for str2 in current_string:
                hashMap[str2] = current_string[count:]
                count += 1

        # Soo.... now I should be able to iterate through meaturedLengths see the lengths of each string based on it's index. Then I just need to find the max?
        for character in measuredLengths:
            length = measuredLengths[character]
            print(f"character: {character}, length: {length} ")
            if length > longest_string:
                longest_string = length

        return longest_string

            


if __name__ == "__main__":
    # Get the directory where this solution.py script lives
    script_dir = Path(__file__).parent
    
    # Join the script's directory with the JSON filename to create a full path
    # Make sure your file is actually named "test_inputs.json"!
    test_file_path = script_dir / "test_inputs.json"
    
    run_tests(Solution, test_file_path)
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
    def romanToInt(self, s: str) -> int:
        return self.pythonic_solution(s)
        return self.match_solution(s)

    def match_solution(self, s: str) -> int:
        str_len = len(s)
        retval = 0
        skip = False
        temp_retval = 0
        for iter in range(0, str_len):
            # When skip is true, we looked ahead one character and know to skip it next time
            if(not skip):
                if(iter + 1 == str_len):
                    # only look at one character
                    debug_str = s[iter]
                    temp_retval, skip = self.roman_lookup(debug_str + " ")
                    retval += temp_retval
                else:
                    debug_str = s[iter:iter+2]
                    temp_retval, skip = self.roman_lookup(debug_str)
                    retval += temp_retval
            else:
                skip = False
        return retval
            
    def roman_lookup(self, char: str):
        match char:
            # Special I cases
            case char if char.startswith("IV"):
                return 4, True
            case char if char.startswith("IX"):
                return 9, True
            # Special X cases
            case char if char.startswith("XL"):
                return 40, True
            case char if char.startswith("XC"):
                return 90, True
            # Special C cases
            case char if char.startswith("CD"):
                return 400, True
            case char if char.startswith("CM"):
                return 900, True
            # Normal Lookups
            case char if char.startswith("I"):
                return 1, False
            case char if char.startswith("V"):
                return 5, False
            case char if char.startswith("X"):
                return 10, False
            case char if char.startswith("L"):
                return 50, False
            case char if char.startswith("C"):
                return 100, False
            case char if char.startswith("D"):
                return 500, False
            case char if char.startswith("M"):
                return 1000, False
            # Error case?
            case _:
                print("Somethig went wrong...")

    def pythonic_solution(self, s: str) -> int:
        # Lookup map
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        for iter in range(len(s)):
            # Check that there is more than 1 character left AND
            # make sure that the next character is not BIGGER than the current character.
            if iter + 1 < len(s) and roman_map[s[iter]] < roman_map[s[iter+1]]:
                total -= roman_map[s[iter]]
            else:
                total += roman_map[s[iter]]

        return total

if __name__ == "__main__":
    # Get the directory where this solution.py script lives
    script_dir = Path(__file__).parent
    
    # Join the script's directory with the JSON filename to create a full path
    # Make sure your file is actually named "test_inputs.json"!
    test_file_path = script_dir / "test_inputs.json"
    
    run_tests(Solution, test_file_path)
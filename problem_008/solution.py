# Extra header to ensure that tests can run individually and as a suite
#  -------------------------------------------------------------------
import sys
from pathlib import Path
# Add the project root folder to the Python path
sys.path.append(str(Path(__file__).resolve().parents[1]))
#  -------------------------------------------------------------------

# Now you can import your wrapper
from test_runner.wrapper import run_tests

MAX_32_BIT_INT = (2**31) -1
MAX_32_BIT_INT_NEGATIVE = -2**(31)

# TODO: this needs a rework to match THEIR description of the algorithm instead of doing it how I think it should be done. Only leading whitespace is removed, etc.
class Solution:
    # We should just have a few simple rules:
    # If you find a character, stop scanning
    # If you find whitespace, discard and keep scanning
    # If you find a negative sign, if number string is empty, add to number string
    # If you find a number, add to number string
    def myAtoi(self, s: str) -> int:
        retval = 0
        numberString = ""
        signFound = False
        for str in s:
            if (str >= "a" and str <= "z") or (str >= "A" and str <= "Z"):
                # Stop scanning
                break
            elif (str == " " or str == "\t" or str == "\n"):
                # Do nothing and move on to the next character
                if(numberString == "") or not signFound:
                    continue
                # If there are already characters in the number string, we have reached the end of the number and stop scanning
                else:
                    break
            elif (str == "-"):
                # If we find more than one sign, stop processing
                if signFound == True:
                    break
                signFound = True
                # If we have a value in the number string (aka not at the beginning of the string) stop processing
                if numberString == "":
                    numberString += str
                else:
                    break
            elif (str == "+"):
                # If we find more than one sign, stop processing
                if(signFound == True):
                    break
                signFound = True
            elif (str >= "0" and str <= "9"):
                numberString += str
            else:
                # unknown character, just stop scanning
                break
            
        print(f"Number string = {numberString}")
        try:
            retval = int(numberString)
        except Exception as e:
            print(f"Exception e = {e}")

        # Cover max and min 32 bit signed integer cases
        if(retval > MAX_32_BIT_INT):
            retval = MAX_32_BIT_INT
        elif(retval < MAX_32_BIT_INT_NEGATIVE):
            retval = MAX_32_BIT_INT_NEGATIVE

        print(f"converted value = {retval}")
        return retval


if __name__ == "__main__":
    # Get the directory where this solution.py script lives
    script_dir = Path(__file__).parent
    
    # Join the script's directory with the JSON filename to create a full path
    # Make sure your file is actually named "test_inputs.json"!
    test_file_path = script_dir / "test_inputs.json"
    
    run_tests(Solution, test_file_path)
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

class Solution:
    def reverse(self, x: int) -> int:
        intAsStr = str(x)
        print(intAsStr)
        reverseIntAsStr = []
        i = len(intAsStr)
        sign = None

        for x in range(i):
            reverseIntAsStr.append("")

        for x in intAsStr:
            i = i - 1
            if(x == "-" or x == "+"):
                # sign symbol found, save it off and remove it from the reversal process
                sign = x
                reverseIntAsStr[0] = x
                i = i + 1
            elif(x >= "0" and x <= "9"):
                # this is a number, so add it to the string
                reverseIntAsStr[i] = x
            else:
                # this is not a number, skip
                continue

        print(reverseIntAsStr)

        finalStr = "".join(reverseIntAsStr)
        print(finalStr)

        retval = int(finalStr)

        # Ensure that the integer we found is within 32 bit signed values (only doing it this way because of the strange way python treats integers. If this was C I would do it very differently.)
        # Cover max and min 32 bit signed integer cases
        if(retval > MAX_32_BIT_INT):
            retval = 0
        elif(retval < MAX_32_BIT_INT_NEGATIVE):
            retval = 0

        return retval


if __name__ == "__main__":
    # Get the directory where this solution.py script lives
    script_dir = Path(__file__).parent
    
    # Join the script's directory with the JSON filename to create a full path
    # Make sure your file is actually named "test_inputs.json"!
    test_file_path = script_dir / "test_inputs.json"
    
    run_tests(Solution, test_file_path)
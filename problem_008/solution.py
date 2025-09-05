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
    # We should just have a few simple rules:
    # If you start with whitespace, process until you don't see whitespace. Repeated whitespace after that means the end of the number.
    # If you see a + or a - it counts as the start of the number, but a second + or - means the end of the number.
    # If you see a number, add it to the string to process. If you see anything else, stop processing and convert the string to a number.
    # If you reach the end of the string, stop processing and convert the string to a number.
    # If the value is greater than a max signed 32 bit integer, round down to a max signed 32 bit integer.
    # If the value is less than a negative max signed 32 bit integer, round up to a negative max signed 32 bit integer.

    def myAtoi(self, s: str) -> int:
        retval = 0
        numberString = ""
        processingLeadingWhiteSpace = True
        signFound = False

        i = -1
        while i + 1 < len(s):
            i = i + 1
            char = s[i]
            # Process leading whitespace
            if processingLeadingWhiteSpace:
                if (char == " " or char == "\t" or char == "\n"):
                    # Do nothing and move on to the next character
                    continue
                else:
                    processingLeadingWhiteSpace = False
            
            # Look for the first instance of a sign character. If we find a sign character for a second time, or we have already found any other non-whitespace character, stop scanning.
            if (char == "+" or char == "-"):
                if signFound == False:
                    signFound = True
                    numberString += char
                    # Scan to the next character because this was a valid sign input
                    continue
                else:
                    # We already found a sign character or already found a number, break out of scanning for more numbers
                    break

            if (char >= "0" and char <= "9"):
                # This is a valid number!
                numberString += char
                # Sign characters after this point are invalid
                signFound = True
            else:
                # Okay we scanned for whitespace, sign characters, and number. Anything found at this point means we found an invalid character for the sequence.
                # Since it is an invalid character, stop scanning.
                break

        # Debug print the number string we found
        print(f"Number string = {numberString}")
        # Try to convert it to an integer
        try:
            retval = int(numberString)
        except Exception as e:
            print(f"Exception e = {e}")

        # Ensure that the integer we found is within 32 bit signed values (only doing it this way because of the strange way python treats integers. If this was C I would do it very differently.)
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
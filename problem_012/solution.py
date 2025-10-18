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
    def intToRoman(self, num: int) -> str:
        int_str = str(num)
        int_order = len(int_str)
        retval = ""
        for char in int_str:
            if(char != "0"):
                retval += self.convert_character(char, 10**(int_order-1))
            # else the next character is 0 so don't do anything
            int_order = int_order - 1
        return retval
    
    def convert_character(self, char: str, multiple: int):
        intermediate = ""
        retval = ""
        match char:
            case '1':
                intermediate = "I"
            case '2':
                intermediate = "II"
            case '3':
                intermediate = "III"
            case '4':
                intermediate = "IV"
            case '5':
                intermediate = "V"
            case '6':
                intermediate = "VI"
            case '7':
                intermediate = "VII"
            case '8':
                intermediate = "VIII"
            case '9':
                intermediate = "IX"
            # case '0':
            #     intermediate = "X"
            #     # Skip returning anything if we are handling the lowest power (aka handle when we have a 0 in the last digit)
            #     if(multiple == 1):
            #         return ""
            case _:
                print("error, a character that is not 0 to 9 was processed somehow...")
        # Now convert the number to the proper scale
        for char in intermediate:
            match char:
                case "I":
                    match multiple:
                        case 1:
                            char = "I"
                        case 10:
                            char = "X"
                        case 100:
                            char = "C"
                        case 1000:
                            char = "M"
                        case _:
                            print("multiple too high case 1")
                case "V":
                    match multiple:
                        case 1:
                            char = "V"
                        case 10:
                            char = "L"
                        case 100:
                            char = "D"
                        case _:
                            print("multiple too high case 2")
                case "X":
                    match multiple:
                        case 1:
                            char = "X"
                        case 10:
                            char = "C"
                        case 100:
                            char = "M"
                case _:
                    print("error case 2")
            retval += char
            
        return retval


if __name__ == "__main__":
    # Get the directory where this solution.py script lives
    script_dir = Path(__file__).parent
    
    # Join the script's directory with the JSON filename to create a full path
    # Make sure your file is actually named "test_inputs.json"!
    test_file_path = script_dir / "test_inputs.json"
    
    run_tests(Solution, test_file_path)
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
    def isMatch(self, s: str, p: str) -> bool:
        current_index = 0
        string_length = len(s)
        pattern_length = len(p)
        pattern_index = 0
        done = False
        retval = False
        last_character = ''

        if('*' not in p):
            if(pattern_length > string_length):
                return False
        while not done:
            incriment_amount = 1
            pattern_incriment_amount = 1
            current_pattern = p[pattern_index]
            match current_pattern:
                case '.':
                    print("Any character")
                    # Since we only accept characters as possible inputs, this should always work and is an easy case
                    # pattern_index += 1
                case '*':
                    print("Any number of last pattern")
                    if(last_character == '.'):
                        # print("repeatedly match any character")
                        # We are matching literally anything...
                        # Two cases:
                        # Nothing else to match, and we just return True
                        if(pattern_index + 1 == pattern_length):
                            return True
                        # Something else to match, so increase until we find the next pattern
                        else:
                            # Okay, if we are not at the end of the pattern and we started with a '.' what do we do?
                            print("ugh deal with this case if it happens")
                            # We could start processing backwards... but I will see what happens if I just do this hack
                            return False
                    else:
                        print("repeatedly match specific character")
                        incriment_amount = moveForwardUntilNoMatch(self, s[current_index:], last_character)
                case _:
                    # print("All other cases")
                    # Two cases here
                    # the next character in the pattern is a * and we could have an empty match
                    try:
                        if(p[pattern_index+1] == '*'):
                            pattern_incriment_amount = 2
                            # Okay, now how many do we actually match?
                            incriment_amount = moveForwardUntilNoMatch(self, s[current_index:], p[pattern_index])
                            # This is very hacky and probably wrong... lets see what happens.
                            if(incriment_amount > 0 and p[pattern_index] == p[incriment_amount-1]):
                                pattern_incriment_amount += 1
                        else:
                            # the next character in the pattern is not a * and we do a normal comparison
                            if(s[current_index] != p[pattern_index]):
                                done = True
                                retval = False
                    except Exception as e:
                        print(f"Exception: {e}")
            last_character = p[pattern_index]
            pattern_index += pattern_incriment_amount
            current_index += incriment_amount
            # Check to see if we have reached the end of the string (or somehow mistakenly increased past the end)
            if(current_index >= string_length):
                done = True
            # Check to see if we have reached the end of the pattern (or somehow mistakenly increased past the end)
            if(pattern_index >= pattern_length):
                done = True
        # If we processed the entire string and reached the end of both the string and the pattern, the regex matched successfully!
        if(current_index == string_length):
            if(pattern_index == pattern_length):
                retval = True
            else:
                # we still have processing to do from the end of the string...
                # Oh god recursion? I hate it but I think it will work...
                retval = self.isMatch(s[current_index-1:], p[pattern_index:])

        # Return the success or failure of the pattern match
        return retval
    
def moveForwardUntilNoMatch(self, s: str, char: str):
    retval = 0
    strlen = len(s)
    try:
        while retval < strlen and s[retval] == char:
            retval += 1
    except Exception as e:
        print(f"exception while moving index forward: {e}")
    return retval

if __name__ == "__main__":
    # Get the directory where this solution.py script lives
    script_dir = Path(__file__).parent
    
    # Join the script's directory with the JSON filename to create a full path
    # Make sure your file is actually named "test_inputs.json"!
    test_file_path = script_dir / "test_inputs.json"
    
    run_tests(Solution, test_file_path)
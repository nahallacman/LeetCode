# Extra header to ensure that tests can run individually and as a suite
#  -------------------------------------------------------------------
import sys
from pathlib import Path
# Add the project root folder to the Python path
sys.path.append(str(Path(__file__).resolve().parents[1]))
#  -------------------------------------------------------------------

# Now you can import your wrapper
from test_runner.wrapper import run_tests

from typing import Dict
import re

class Solution:
    def sortedWordCount(self, s: str) -> Dict[str, int]:
        retval = {}
        # Tokenize the input into words. Split on syntax and punctuation.

        token_array =  re.findall(r'\b\w+\b', s)
        for token in token_array:
            token_lower = str.lower(token)
            try:
                retval[token_lower] += 1
            except:
                retval[token_lower] = 1

        return retval

if __name__ == "__main__":
    # Get the directory where this solution.py script lives
    script_dir = Path(__file__).parent
    
    # Join the script's directory with the JSON filename to create a full path
    # Make sure your file is actually named "test_inputs.json"!
    test_file_path = script_dir / "test_inputs.json"
    
    run_tests(Solution, test_file_path)
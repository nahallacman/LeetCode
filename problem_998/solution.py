# Extra header to ensure that tests can run individually and as a suite
#  -------------------------------------------------------------------
import sys
from pathlib import Path
# Add the project root folder to the Python path
sys.path.append(str(Path(__file__).resolve().parents[1]))
#  -------------------------------------------------------------------

# Now you can import your wrapper
from test_runner.wrapper import run_tests

import re

class Solution:
    def mostNotBanned(self, paragraph: str, banned: str) -> str:
        # Tokenize the input
        word_list = re.findall(r"[a-zA-Z]+", paragraph.lower())
        banned_word_list = re.findall(r"[a-zA-Z]+", banned.lower())

        # Dictionary of all words and their associated counts
        word_dict = {}

        # Count each word
        for word in word_list:
            try:
                word_dict[word] = word_dict[word] + 1
            except:
                word_dict[word] = 1

        # Remove the filtered words
        filtered_words = {
            key: value for key, value in word_dict.items() 
            if key not in banned_word_list
        }

        # Now that we have a list that filtered out the banned words, return the biggest count word
        word = max(filtered_words, key=filtered_words.get)

        print(f"word that was used the most and was not banned = {word}")

        return word


if __name__ == "__main__":
    # Get the directory where this solution.py script lives
    script_dir = Path(__file__).parent
    
    # Join the script's directory with the JSON filename to create a full path
    # Make sure your file is actually named "test_inputs.json"!
    test_file_path = script_dir / "test_inputs.json"
    
    run_tests(Solution, test_file_path)
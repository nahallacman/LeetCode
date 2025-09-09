# Extra header to ensure that tests can run individually and as a suite
#  -------------------------------------------------------------------
import sys
from pathlib import Path
# Add the project root folder to the Python path
sys.path.append(str(Path(__file__).resolve().parents[1]))
#  -------------------------------------------------------------------

# Now you can import your wrapper
from test_runner.wrapper import run_tests

from collections import defaultdict

class Solution:
    # You’ll be given a list where the value at each index represents the size of the group that person belongs to. Your task is to group people into lists of the correct size.
    def groupBasedOnID(self, group_size_list: str) -> list[list]:
        retval = []
        group_size_dict = defaultdict(list)
        index = 0
        for person in group_size_list:
            try:
                person_int = int(person)
                group_size_dict[person_int].append(index)
                # increase count for each loop
                index = index + 1
            except:
                pass

        # Sort the dictionary by key size
        sorted_groups = sorted(group_size_dict.items())

        for group, list_index in sorted_groups:
            while list_index:
                iter = 0
                temp_list = []
                while iter < group:
                    temp_list.append(list_index.pop(0))
                    iter = iter + 1
                retval.append(temp_list)

        return retval


if __name__ == "__main__":
    # Get the directory where this solution.py script lives
    script_dir = Path(__file__).parent
    
    # Join the script's directory with the JSON filename to create a full path
    test_file_path = script_dir / "test_inputs.json"
    
    run_tests(Solution, test_file_path)
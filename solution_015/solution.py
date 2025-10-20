# Extra header to ensure that tests can run individually and as a suite
#  -------------------------------------------------------------------
import sys
from pathlib import Path
# Add the project root folder to the Python path
sys.path.append(str(Path(__file__).resolve().parents[1]))
#  -------------------------------------------------------------------

# Now you can import your wrapper
from test_runner.wrapper import run_tests
from typing import List
import copy

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Set up return
        retval = []
        nums_len = len(nums)
        # if(nums_len < 3 or nums_len > 3000):
        #     return retval
        j_nums_len = nums_len - 1
        done = False
        i = 0
        j = 1
        k = 2
        new_list = []

        while(not done):
            if (nums[i] + nums[j] + nums[k] == 0):
                # sort the numbers so it goes smallest, middle, biggest
                new_list = [nums[i], nums[j], nums[k]]
                new_list.sort()
                # Prevent duplicates
                if( new_list not in retval ):
                    retval.insert(0, new_list)
            # move k forward one
            k = k + 1
            # If k has reached the end of the array,
            if(k >= nums_len):
                # move j forward one
                j = j + 1
                # If j has reached 1 away from the end of the array
                if(j >= j_nums_len):
                    # move the entire pointer set back to the start of the array, but not losing the index we had for i
                    i = i + 1
                    j = i + 1
                # reset k to be just 1 ahead of j
                k = j + 1
                if(k >= nums_len):
                    done = True

        # print(f"retval = {retval}")
        
        return retval


if __name__ == "__main__":
    # Get the directory where this solution.py script lives
    script_dir = Path(__file__).parent
    
    # Join the script's directory with the JSON filename to create a full path
    # Make sure your file is actually named "test_inputs.json"!
    test_file_path = script_dir / "test_inputs.json"
    
    run_tests(Solution, test_file_path)
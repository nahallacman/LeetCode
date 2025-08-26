# Extra header to ensure that tests can run individually and as a suite
#  -------------------------------------------------------------------
import sys
from pathlib import Path
# Add the project root folder to the Python path
sys.path.append(str(Path(__file__).resolve().parents[1]))
#  -------------------------------------------------------------------

# Now you can import your wrapper
from test_runner.wrapper import run_tests

# Imports for the solution
from typing import List

class Solution:
    # C style Brute force n log n option
    def __twoSum(self, nums: List[int], target: int) -> List[int]:
        retval = []
        
        # [0] [1] [2] [3]
        #     [1] [2] [3]
        #         [2] [3]

        # three pointers
        # start of array
        # first number to check
        # second number to check
        index_start_array = 0
        array_max_size = len(nums)
        done = False
        done_inner_loop = False
        # Loop over everything, starting at the start of the array
        while not done:
            done_inner_loop = False

            # Reset the comparison pointers, always moving them forward through the array
            index_first_num = index_start_array
            index_second_num = index_first_num + 1
            while not done_inner_loop:
                # Compare the numbers at the index to see if they match the expected result
                if(nums[index_first_num] + nums[index_second_num] == target):
                    retval = [index_first_num, index_second_num]
                    done_inner_loop = True
                else:
                    # We didn't find the right answer, so increase the index to try again.
                    index_second_num = index_second_num + 1

                    if(index_second_num == array_max_size):
                        done_inner_loop = True

            index_start_array = index_start_array + 1
            
            if retval != []:
                done = True

        return retval
    
    # pythonic style Brute force option n log n I think, no early exits
    def __twoSum(self, nums: List[int], target: int) -> List[int]:
        retval = []

        for i, num in enumerate(nums):
            for j, num2 in enumerate(nums[i+1:], i+1):
                if num + num2 == target:
                    retval = [i, j]

        return retval
    
    # pythonic style Brute force option n log n I think, early exits
    def __twoSum(self, nums: List[int], target: int) -> List[int]:
        retval = []

        for i, num in enumerate(nums):
            for j, num2 in enumerate(nums[i+1:], i+1):
                if num + num2 == target:
                    return [i, j]

        return retval
    
    # pythonic style Brute force option n log n I think, early exits
    def __twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            for j, num2 in enumerate(nums[i+1:], i+1):
                if num + num2 == target:
                    return [i, j]

        return None
    
    # Hash map solution from Gemini
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Finds two numbers in a list that sum up to a target value.

        Args:
        nums: A list of integers.
        target: The target integer sum.

        Returns:
        A list containing the indices of the two numbers.
        """
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

if __name__ == "__main__":
    # Get the directory where this solution.py script lives
    script_dir = Path(__file__).parent
    
    # Join the script's directory with the JSON filename to create a full path
    # Make sure your file is actually named "test_inputs.json"!
    test_file_path = script_dir / "test_inputs.json"
    
    run_tests(Solution, test_file_path)
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
        # return self.threeSumNSquared(nums)
        return self.threeSumNSquared_try_2(nums)
        # return self.threeSumNCubed(nums)

    # This worked fine when the values were small... 
    def threeSumNCubed(self, nums: List[int]) -> List[List[int]]:
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
    
    # This has a bug in it I don't understand...
    def threeSumNSquared(self, nums: List[int]) -> List[List[int]]:
        nums_sorted = nums
        nums_sorted.sort()
        nums_len = len(nums)
        retval = []

        i = 0
        j = 0
        k = 0
        done = False
        while(not done):
            # # Start at the beginning of i
            start = i
            # Move i forward until it is the last of it's identical copies
            while(nums_sorted[start] == nums_sorted[i]):
                i = i + 1
            # Now i points at a value that has no copies after it
            # Get a pair of values that sums to the value of -i, so -i = j + k
            target_value = -nums_sorted[i]
            offset = i + 1
            sum_results = self.twoSum(nums_sorted[offset:], target_value)
            print(f"sum_results = {sum_results}")
            if(sum_results):
                j = sum_results[0] + offset
                k = sum_results[1] + offset
                a = nums_sorted[i]
                b = nums_sorted[j]
                c = nums_sorted[k]

                # Now we have a valid entry for i, j, k, add it to the return list, 
                retval.append([a, b, c])
            # incriment i, and start over if we aren't done yet
            i = i + 1
            if(i > nums_len - 2):
                done = True
        
        return retval

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

    def threeSumNSquared_try_2(self, nums: List[int]) -> List[List[int]]:
        retval = []
        # adds nlog(n) complexity
        nums.sort()

        # add n^2 complexity
        for i, a in enumerate(nums):
            # Skip if the value isn't the same as the last value we tried to use
            # Also don't do this on the first try so we don't get an index error
            if i > 0 and a == nums[i - 1]:
                continue

            # Initialize your pointers
            left, right = i + 1, len(nums) - 1
            # As long as the left pointer is to the left of the right pointer
            while left < right:
                threeSum = a + nums[left] + nums[right]
                # If our sum is bigger than zero, we need to move the right pointer left (as there will be smaller numbers to the left of it)
                if threeSum > 0:
                    right -= 1
                # If  our sum is smaller than zero, we need to move the left pointer right (as there will be bigger numbers to the right of it)
                elif threeSum < 0:
                    left += 1
                # We have an answer of exactly 0, so add the answer to the list
                else:
                    retval.append([a, nums[left], nums[right]])
                    # Now move the left pointer at least one to the right
                    left += 1
                    # and if there are identical values to the right, and we are still less than the right pointer, move the pointer right
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return retval




if __name__ == "__main__":
    # Get the directory where this solution.py script lives
    script_dir = Path(__file__).parent
    
    # Join the script's directory with the JSON filename to create a full path
    # Make sure your file is actually named "test_inputs.json"!
    test_file_path = script_dir / "test_inputs.json"
    
    run_tests(Solution, test_file_path)
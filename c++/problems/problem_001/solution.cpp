#include "solution.hpp"

// Standard LeetCode solution for Two Sum
std::vector<int> Solution::twoSum(std::vector<int>& nums, int target) {
    // Input: nums = [2,7,11,15], target = 9
    // Output: [0,1]
    // Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

    for(auto it=nums.begin(); it != nums.end(); ++it){
        for(auto j=(it + 1); j != nums.end(); ++j){
            if(*it + *j == target) {
                auto retval = std::vector<int>();
                int index = std::distance(nums.begin(), it);
                int index2 = std::distance(nums.begin(), j);
                retval.push_back(index);
                retval.push_back(index2);
                return retval;
            }
        }
    }

    return std::vector<int>(); // Should not happen for valid inputs
}
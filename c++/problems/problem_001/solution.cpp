#include "solution.hpp"

#include <iostream>

#include <unordered_map>

// // Standard LeetCode solution for Two Sum
// std::vector<int> Solution::twoSum(std::vector<int>& nums, int target) {
//     // Input: nums = [2,7,11,15], target = 9
//     // Output: [0,1]
//     // Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

//     for(auto it=nums.begin(); it != nums.end(); ++it){
//         for(auto j=(it + 1); j != nums.end(); ++j){
//             if(*it + *j == target) {
//                 auto retval = std::vector<int>();
//                 int index = std::distance(nums.begin(), it);
//                 int index2 = std::distance(nums.begin(), j);
//                 retval.push_back(index);
//                 retval.push_back(index2);
//                 return retval;
//             }
//         }
//     }

//     return std::vector<int>(); // Should not happen for valid inputs
// }

// // Using the red/black tree to store the values and their indexes to have a nlogn lookup 
// std::vector<int> Solution::twoSum(std::vector<int>& nums, int target) {
//     // Input: nums = [2,7,11,15], target = 9
//     // Output: [0,1]
//     // Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
//     std::map<int, int> lookup;
//     auto index = 0;
//     for(auto it = nums.begin(); it != nums.end(); it++, index++){
//         int local_target = target - *it;
//         auto found = lookup.find(local_target);
//         if(found != lookup.end()){
//             // If we find a value that the math check will return, now we just need to get the index of the current iterator and the value of the iteratior stored in the map.
//             std::vector<int> retval = std::vector<int>();
//             retval.push_back(index);
//             retval.push_back(found->second);
//             return retval;
//         } else {
//             lookup.insert({*it, index});
//         }
//     }

//     return std::vector<int>(); // Should not happen for valid inputs
// }

// TODO: do it with an unordred map
std::vector<int> Solution::twoSum(std::vector<int>& nums, int target) {

    std::unordered_map<int, int> valueToFind;
    int first = -1;
    int second = -1;

    for( int it = 0; it < nums.size(); it++ ){
        int calc = target - nums[it];
        valueToFind[calc] = it;
    }
    
    for( int it = 0; it < nums.size(); it++ ) {
        if( valueToFind.find(nums[it]) != valueToFind.end() ){
            if( valueToFind[nums[it]] != it ) {
                first = valueToFind[nums[it]];
                second = it;
                break;
            }
        }
    }
    std::vector<int> retval;
    retval.push_back(first);
    retval.push_back(second);
    return retval;
}
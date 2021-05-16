"""

46. Permutations
Medium

6035

135

Add to List

Share
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
 

Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
Accepted
815,191
Submissions
1,207,578

"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 2:
            return [nums]
        result = []
        for i in range(len(nums)):
            temp_nums = nums[:]
            num = temp_nums.pop(i)
            crazy_shit = self.permute(temp_nums)    
            for crazy in crazy_shit:
                result.append([num] + crazy)
        
        return result
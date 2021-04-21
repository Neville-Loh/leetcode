"""
42. Trapping Rain Water
Hard

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
0 <= n <= 3 * 104
0 <= height[i] <= 105



"""

"""
C = O(n)
M = O(n)
"""
class Solution:
    def trap(self, nums: List[int]) -> int:
        total_water = 0
        max_left_walls = [0] * len(nums)
        max_right_walls = [0] * len(nums)

        current_max = 0
        for i in range(1,len(nums)):
            if nums[i-1] > current_max:
                current_max = nums[i-1]
            max_left_walls[i] = current_max

        current_max = 0
        for i in range(len(nums)-2,-1,-1):
            if nums[i+1] > current_max:
                current_max = nums[i+1]
            max_right_walls[i] = current_max
        
        ## finding block water
        for i, num in enumerate(nums):
            block_water = min(max_left_walls[i], max_right_walls[i]) - num
            if block_water > 0:
                total_water += block_water
            
        return total_water
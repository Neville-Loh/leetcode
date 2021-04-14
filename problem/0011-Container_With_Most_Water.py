"""
11. Container With Most Water
Medium


Given n non-negative integers a1, a2, ..., an , 
where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) 
and (i, 0). Find two lines, which, together with the x-axis forms a container, such 
that the container contains the most water.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1
Example 3:

Input: height = [4,3,2,1,4]
Output: 16
Example 4:

Input: height = [1,2,1]
Output: 2
 

Constraints:

n == height.length
2 <= n <= 10^5
0 <= height[i] <= 10^4



"""

import sys
from typing import List

# You are given an arrya of postive integers where each interger 
# represents the height of a vertical line on a chart. 

# Find two lines which together with the x-axis forms a container
# that would hold the greatest amount of water. Return the area of water
# it would hold

#[1,8,6,2,9,4]

# algo design
L = [1,8,6,2,5,4,8,3,7]


# O(n^2) brute force
def max_area(nums):
    result = None
    current_max = 0
    for i, num in enumerate(nums):
        # keeping track of max
        # area = (j-i) * (min(num[j],num[i]))
        # keeping track of low
        print(i, num)
        for j, num2 in enumerate(nums[i:], start=i):
            area = (j-i) * min(num, num2)
            if area > current_max:
                current_max = area
                result = (i,j)
    return current_max




# O(n)
class Solution:
    def maxArea(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        current_max = 0

        while (left < right):
            area = min(nums[left],nums[right]) * (right - left)
            current_max = max(current_max,area)

            if nums[left] < nums[right]:

                left += 1
            else:
                right -= 1
        return current_max


s = Solution()
print(s.maxArea(L))

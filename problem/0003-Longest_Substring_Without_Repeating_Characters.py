"""

3. Longest Substring Without Repeating Characters
Medium

Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

Author: Neville
Date: 19 May 2021
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        start = 0
        char_map = {}

        for i in range(len(s)):
            char = s[i]
            if char in char_map:
                # save current string
                result = max(result, i- start)
                
                # adjust start at last repeat
                if char_map[char] + 1 > start:
                    start = char_map[char] + 1
                    
            char_map[char] = i
        
        result = max(len(s) - start, result)
        return result
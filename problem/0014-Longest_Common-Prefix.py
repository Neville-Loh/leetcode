"""
14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.

Author:Neville
Date: Sept 30 2020
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        brute force
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        letter_int = 0
        while len(strs) > 0 and letter_int < len(strs[0]):
            for s in strs[1:]:
                if letter_int >= len(s):
                    return result

                if s[letter_int] != strs[0][letter_int]:
                    return result
            result = result + strs[0][letter_int]
            letter_int = letter_int + 1
            
        return result
        
    def longestCommonPrefix2ndAttempt(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ""
        if len(strs) == 1: return strs[0]
        
        strs.sort()
        p = ""
        for x, y in zip(strs[0], strs[-1]):
            if x == y: p+=x
            else: break
        return r
            
        

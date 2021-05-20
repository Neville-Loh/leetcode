"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.


Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.


Author: Neville
Date: 20 May 2021
"""

class Solution:
    def validPalindrome(self, s: str, remove_char=1) -> bool:
        if len(s) <= 1:
            return True
        elif s[0]==s[-1]:
            return self.validPalindrome(s[1:-1], remove_char=remove_char)
        elif remove_char > 0:
            return (self.validPalindrome(s[0:-1], remove_char=(remove_char-1)) or
                    self.validPalindrome(s[1:], remove_char=(remove_char-1))
                    )
        else:
            return False

    def validPalindrome2(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        elif s[0]==s[-1]:
            return self.validPalindrome(s[1:-1])
        else:
            return (s[0:-1] ==  s[-2::-1]) or (s[1:] == s[:0:-1])
        

"""
# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Author : Neville Loh
Date: 30 Aug 2020
"""
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        
        if len(s) <= 1:
            return True
        elif s[0] == s[-1]:
            return self.isPalindrome(s[1:-1])
        else:
            return False

    """
    Shorter version of the above code.
    """
    def isPalindromeShort(self, x):
        return str(x) == str(x)[::-1]

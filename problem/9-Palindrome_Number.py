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

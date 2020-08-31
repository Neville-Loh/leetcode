class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = "1"
        result = ["1",]
        i = 1
        while i <= n:
            L = [m.group(0) for m in re.finditer(r"(\d)\1*", result[i-1])]
            my_str = ""
            for num in L:
                my_str +=(str(len(num)) + num[0])
            result.append(my_str)
            i += 1

        return result[n-1]
        

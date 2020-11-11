"""
0118. Pascal's Triangle

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
Accepted
427,099
Submissions
795,312

"""
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for n in range(numRows):
            if n == 0:
                result.append([1])
            elif n == 1:
                result.append([1,1])
            else:
                lastRow = result[-1]
                newRow = [1,]
                for i in range(len(lastRow)-1):
                    newRow.append(lastRow[i]+lastRow[i+1])
                newRow.append(1)
                result.append(newRow)
        
        
        return result

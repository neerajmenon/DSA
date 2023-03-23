#LC118
#PascalTriangle
#Input: numRows = 5
#Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

class Solution(object):
    def generate(self, numRows):
        res = [[1]]
        for i in range(1, numRows):
            temp1 = res[-1] + [0]
            temp2 = [0] + res[-1]
            res.append([temp1[i]+temp2[i] for i in range(len(temp1))])
        return res[:numRows]
        
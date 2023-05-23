

#DP
class Solution:
    def climbStairs(self, n: int) -> int:
        p,q=1,1
        for i in range(n-1):
            temp = p
            p = p+q
            q = temp
        return p
class Solution:
    def letterCombinations(self, digits):
        hm = {2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
        res = []
        def dfs(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for c in hm[int(digits[i])]:
                dfs(i + 1, curStr + c)

        if digits:
            dfs(0, "")

        return res
    
s = Solution()
res = s.letterCombinations("633725") #hehe my name encoded
print(res)
print(res.index("neeraj"))
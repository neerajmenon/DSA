class Solution:
    def combinationSum(self, candidates, target):
        res = []
        subset = []
        def dfs(i,target):
            if target == 0:
                res.append(subset.copy())
                return
            if i >= len(candidates) or target < 0:
                return
            
            subset.append(candidates[i])
            dfs(i,target-candidates[i])
            subset.pop()
            dfs(i+1,target)

        dfs(0,target)
        return res
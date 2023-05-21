class Solution:
    def combinationSum2(self, candidates, target):
        res = []
        subset = []
        candidates.sort()
        def dfs(i,target):
            if target == 0:
                res.append(subset.copy())
                return
            if i >= len(candidates) or target < 0:
                return
            
            subset.append(candidates[i])
            dfs(i+1,target-candidates[i]) # i+1 not i here, as no  repicks this time
            subset.pop()
            while (i+1)<len(candidates) and candidates[i+1]==candidates[i]:
                    i+=1
            dfs(i+1,target)

        dfs(0,target)
        return res
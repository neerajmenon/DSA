class Solution:
    def permute(self, nums):
        res = []
        def dfs(i):
            if i >= len(nums):
                res.append(nums[:])
            else:
                for k in range(i,len(nums)):
                    nums[i],nums[k] = nums[k],nums[i]
                    dfs(i+1)
                    nums[i],nums[k] = nums[k],nums[i]
        dfs(0)
        return res
"""
input:    
[1,2,3]

callstack:

i=0,k=0
swap(0,0)->nochange
dfs(i=1)
i=1, k=1
swap(1,1)->nochange
dfs(i=2)
i=2,k=2
swap(2,2)->nochange
dfs(i=3)
res = [[1,2,3]]
<ret dfs(i=3)
unswap(2,2)->nochange
<ret dfs(i=2) 
i=1,k=1
unswap(1,1)->nochange
i=1,k=2
swap(1,2)->[1,3,2]
dfs(i=2)
i=2,k=2
swap(2,2)->nochange
dfs(i=3)
res = [[1,2,3],[1,3,2]]
<ret dfs(i=3)
unswap(2,2)->nochange
<ret dfs(i=2)
unswap(1,2)->[1,2,3]=
<ret dfs(i=1)
unswap(0,0)->nochange
i=0,k=1
swap(0,1)->[2,1,3]
dfs(i=1)
i=1,k=1
swap(1,1)->nochange
dfs(i=2)
i=2,k=2
swap(2,2)->nochange
dfs(i=3)
res = [[1,2,3],[1,3,2],[2,1,3]]
<ret dfs(i=3)
unswap(2,2)->nochange
<ret dfs(i=2)
unswap(1,1)->nochange
i=1,k=2
swap(1,2)->[2,3,1]
dfs(i=2)
swap(2,2)
dfs(i=3)
res->[[1,2,3],[1,3,2],[2,1,3],[2,3,1]]
< ret dfs(i=3)
unswap(2,2)
< ret dfs(i=2)
unswap(1,2)->[2,1,3]
< ret dfs(i=1)
unswap(0,1)->[1,2,3]
i=0,k=2
swap(0,2)->[3,2,1]
dfs(i=1):
swap(1,1)->nochange
dfs(i=2)
swap(2,2)->nochange
dfs(i=3)
res->[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,2,1]]
< ret dfs(i=3)
unswap(2,2)->nochange
< ret dfs(i=2)
unswap(1,1)->nochange
i=1, k=2
swap(1,2)->[3,1,2]
dfs(i=2)
swap(2,2)->nochange
dfs(i=3)
res->[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,2,1],[3,1,2]]
< ret dfs(i=3)
unswap(2,2)
< ret dfs(i=2)
unswap(1,1)
< ret dfs(i=1)
unswap(0,2)->[1,2,3] # back to original
< ret dfs(0) 











"""
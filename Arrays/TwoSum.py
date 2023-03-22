#LC-1
#TwoSum
#v1 : no sort, return indices
#v2 : sort, two pointers, return values
class Solution(object):
    def twoSum(self, nums, target):
        hm = dict()
        for i in range(0,len(nums)):
            rem_idx = hm.get(target-nums[i])
            if rem_idx is not None:
                return [i,hm.get(target-nums[i])]
            hm.update({nums[i]:i})
            
class Solution(object):
    def twoSum(self, nums, target):
        nums.sort()
        i = 0
        j = len(nums)-1
        while(i<=j):
            sum = nums[i] + nums[j]
            if sum == target:
                return [nums[i],nums[j]]
            if sum > target:
                j-=1
            if sum < target:
                i+=1
        return [None,None]
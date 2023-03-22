#LC-513 

class Solution(object):
    def maxSubArray(self, nums):
        currentMax = nums[0]
        maxSoFar = nums[0]
        for i in range(1,len(nums)):
            currentMax += nums[i]
            if currentMax < nums[i]:
                currentMax = nums[i]
            if maxSoFar < currentMax:
                maxSoFar = currentMax
        return maxSoFar
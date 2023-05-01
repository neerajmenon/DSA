#LC-169

#O(1) space solution
class Solution(object):
    def majorityElement(self, nums):

        arr = nums.sort()
        return nums[len(nums)/2]
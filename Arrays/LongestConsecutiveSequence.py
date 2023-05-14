# O(n) time and space
class Solution(object):
    def longestConsecutive(self, nums):
        longest = 0
        num_set = set(nums)

        for n in nums:
            if (n-1) not in num_set:
                length=0
                while (n+length) in num_set:
                    length+=1
                longest = max(length,longest)
        
        return longest
    
# O(nlog(n)) time O(1) space    
class Solution:
    def longestConsecutive(self, nums):
        if len(nums) == 0:
            return 0
        nums.sort()
        max_length = 1
        current_length = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] - nums[i-1] == 1:
                    current_length += 1
                else:
                    max_length = max(max_length, current_length)
                    current_length = 1
        return max(max_length, current_length)
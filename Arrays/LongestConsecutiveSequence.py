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
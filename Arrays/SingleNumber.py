#LC-136
class Solution(object):
    def singleNumber(self, nums):
        
        seen = set()
        for x in nums:
            if x in seen:
                seen.remove(x)
            else:
                seen.add(x)
                
        return seen.pop()
                
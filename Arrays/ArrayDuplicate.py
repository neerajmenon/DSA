#LC-217
#Check if array contains duplicates
class Solution(object):
    def containsDuplicate(self, nums):
        unq = set()
        for x in nums:
            if x not in unq:
                unq.add(x)
            else:
                return True
        return False
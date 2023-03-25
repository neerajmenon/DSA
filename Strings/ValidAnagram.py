#LC-242

class Solution(object):
    def isAnagram(self, s, t):
        counts = dict()
        for s in s:
            counts[s] = counts.get(s, 0) + 1
        for s in t:
            counts[s] = counts.get(s, 0) - 1

        for val in counts.values():
            if val != 0 :
                return False
        return True
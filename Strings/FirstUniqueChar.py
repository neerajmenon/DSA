#LC-387 
#First Unique Character in a String

from collections import OrderedDict

class Solution(object):
    def firstUniqChar(self, s):

        counts = OrderedDict()
        for i in range(0,len(s)):
            counts[s[i]] = counts.get(s[i], 0) + 1

        for key, value in counts.items():
            if value == 1:
                return s.find(key)
        return -1
class Solution(object):
    def groupAnagrams(self, strs):
        hm = {}
        for x in strs:
            sorted_x = ''.join(sorted(x))
            hm[sorted_x] = hm.get(sorted_x,[])
            hm[sorted_x].append(x)
        return hm.values()
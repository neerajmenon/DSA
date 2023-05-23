class Solution(object):
    def minWindow(self, s, t):
        t_hm = {}
        s_hm = {}
        for x in t:
            t_hm[x] = t_hm.get(x, 0) + 1
        l, r = 0, 0
        res_c = float('inf')
        res = ""
        while r < len(s):
            s_hm[s[r]] = s_hm.get(s[r], 0) + 1
            r += 1
            while l < r and all(s_hm.get(char, 0) >= count for char, count in t_hm.items()):
                if r - l < res_c:
                    res_c = r - l
                    res = s[l:r]
                s_hm[s[l]] -= 1
                if s_hm[s[l]] == 0:
                    del s_hm[s[l]]
                l += 1

        return res
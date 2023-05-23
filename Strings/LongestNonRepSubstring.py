class Solution(object):
    def lengthOfLongestSubstring(self, s):
        hs = set()
        longest = 0
        l,r=0,0
        while r<len(s):
            while s[r] in hs:
                hs.remove(s[l])
                l+=1
            
            hs.add(s[r])
            longest = max(longest,r-l+1)
            r+=1
        
        return longest
                

        
def longestSubstringWithKDistinctChars(k, s):
    hm = {}
    l,r=0,0
    res = 0
    while r<len(s):
        hm[s[r]] = hm.get(s[r],0) + 1
        if max(hm.values())>1 or len(hm.values())>k:
            hm[s[l]]-=1
            if hm[s[l]] == 0:
                del hm[s[l]]
            l+=1
        res = max(res,r-l+1)
        r+=1
    return res



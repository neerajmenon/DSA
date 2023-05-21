def generate_subsequences(s):
    res = []
    subs = []
    def dfs(i):
        if i == len(s):
            res.append("".join(subs))
            return
        subs.append(s[i])
        dfs(i+1)
        subs.pop()
        dfs(i+1)

    dfs(0)
    return res

s="abc"
res = generate_subsequences(s)
print(res)
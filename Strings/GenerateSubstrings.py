def generate_substrings(s):
    substrings = []
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n + 1):
            substrings.append(s[i:j])
            #print(i,j,s[i:j])
    return substrings


s = "abc"
substrings = generate_substrings(s)
print(substrings)

"""
"abc"
0 1 a
0 2 ab
0 3 abc
1 2 b
1 3 bc
2 3 c
['a', 'ab', 'abc', 'b', 'bc', 'c']
"""
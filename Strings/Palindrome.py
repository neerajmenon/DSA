class Solution(object):
    def isPalindrome(self, s):
        s = re.sub(r'[^a-zA-Z]', '', s).lower()
        l,r = 0,len(s)-1
        while(l<=r):
            if s[l]!=s[r]:
                return False
            else:
                l+=1
                r-=1
        return True



def is_palindrome(string):
    return string == string[::-1]

def check_palindrome_substrings(input_string, queries):
    results = []
    for query in queries:
        start, end = query
        substring = input_string[start:end+1]
        is_palindrome_flag = is_palindrome(substring)
        results.append(is_palindrome_flag)
    return results

# Example usage:
input_string = "abaaabaaaba"
queries = [[0, 10], [5, 8], [2, 5], [5, 9]]
results = check_palindrome_substrings(input_string, queries)
print(results)

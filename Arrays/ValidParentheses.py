#LC-20
class Solution(object):
    def isValid(self, s):
        stack = []
        for x in s:
            if x == '(' or x == '[' or x == '{':
                stack.append(x)
            elif x == ')' and len(stack)>0 and stack[-1] == '(':
                stack.pop()
            elif x == ']' and len(stack)>0 and stack[-1] == '[':
                stack.pop()
            elif x == '}' and len(stack)>0 and stack[-1] == '{':
                stack.pop()
            else:
                return False

        return len(stack) == 0 
    

#With hashmap
class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()

        return not stack

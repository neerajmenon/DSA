#LC-144
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        arr = []
        def dfs(root):
            if root != None:
                arr.append(root.val)
                dfs(root.left)
                dfs(root.right)
        
        dfs(root)
        return arr
    
#Iterative
class Solution(object):
    def preorderTraversal(self, root):
        res = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        
        return res
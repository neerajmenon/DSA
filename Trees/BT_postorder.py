# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        res = []
        def dfs(root):
            if root:
                dfs(root.left)
                dfs(root.right)
                res.append(root.val)

        dfs(root)
        return res
    
class Solution(object):
    def postorderTraversal(self, root):
        res = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        
        return res[::-1]

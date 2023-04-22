# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        arr=[]
        def dfs(root):
            if root:
                dfs(root.left)
                arr.append(root.val)
                dfs(root.right)
        
        dfs(root)
        return arr
    
class Solution(object):
    def inorderTraversal(self, root):
        res = []
        stack = []
        
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        
        return res

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def diameterOfBinaryTree(self, root):
        res = 0
        def dfs(root):
            nonlocal res
            if root:
                l = dfs(root.left)
                r = dfs(root.right)
                paththru = l + r
                res = max(res,paththru)
                return 1 + max(l,r)
            return 0

        dfs(root)
        return res
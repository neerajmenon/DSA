# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        s = set()
        def dfs(root):
            if root:
                if (k - root.val) in s:
                    return True
                s.add(root.val)
                return dfs(root.left) or dfs(root.right)
            return False
        return dfs(root)
        
        
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        arr = []
        def dfs(root):
            if root:
                dfs(root.left)
                arr.append(root.val)
                dfs(root.right)
        dfs(root)
        return arr[k-1]

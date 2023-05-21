# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root, subroot):
        if not subroot:
            return True
        if not root:
            return False

        if self.isSameTree(root, subroot):
            return True
        return self.isSubtree(root.left, subroot) or self.isSubtree(root.right, subroot)

    def isSameTree(self, p,q):
        if p and q:
            l = self.isSameTree(p.left,q.left)
            r = self.isSameTree(p.right,q.right)
            vals = p.val == q.val
            return l and r and vals
        if p or q:
            return False
        return True
        
        
    
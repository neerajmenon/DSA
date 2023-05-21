# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root):

        def height(root):
            if root:
                l_bal, l = height(root.left)
                r_bal, r = height(root.right)
                balanced = l_bal and r_bal and abs(l-r)<=1
                return[balanced,1+max(l,r)]
            return [True,0]

        res, h = height(root)
        return res
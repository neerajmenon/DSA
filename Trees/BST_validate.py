# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        arr = []
        def dfs(root):
            if root:
                dfs(root.left)
                arr.append(root.val)
                dfs(root.right)

        dfs(root)
        for i in range(0,len(arr)-1):
            if arr[i+1]<=arr[i]:
                return False
        return True
            
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        l = float("-inf")
        h = float("inf")
        def dfs(root,l,h):
            if root:
                if root.val >= h or root.val <= l:
                    return False
                return dfs(root.left,l,root.val) and dfs(root.right,root.val,h)
            return True

        return dfs(root,l,h)
            
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
    
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        arr=[]
        s=[] #Stack

        while root:
            
            if len(s)>0 and s[-1]==root:
                s.pop()

            elif root.left:
                s.append(root)
                root = root.left
                continue
            arr.append(root.val)
            if root.right:
                root = root.right
                continue

            if len(s)>0:
                root = s[-1]
            else:
                break


        return arr
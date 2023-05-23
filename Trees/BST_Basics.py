def insertIntoBST(self, root, val):
        if root:
            if val < root.val:
                root.left = self.insertIntoBST(root.left,val)
            elif val > root.val:
                root.right = self.insertIntoBST(root.right,val)
            return root
        return TreeNode(val=val)

def searchBST(self, root, val):
        if root:
            if root.val == val:
                return root
            elif root.val > val:
                return self.searchBST(root.left,val)
            else:
                return self.searchBST(root.right,val)
        return None
    
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
    
def kthSmallest(self, root, k): #inorder of BST is sorted 
        arr = []
        def dfs(root):
            if root:
                dfs(root.left)
                arr.append(root.val)
                dfs(root.right)
        dfs(root)
        return arr[k-1]

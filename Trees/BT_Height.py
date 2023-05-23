def maxDepth(self, root):
        if root:
            return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
        return 0

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
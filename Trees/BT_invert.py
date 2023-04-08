class Solution:
    def invertTree(self, root):
        if root:
            left = self.invertTree(root.left)
            right = self.invertTree(root.right)
            root.left = right
            root.right = left
            return root

        return None
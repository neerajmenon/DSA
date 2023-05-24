def countLeaves(root):
    if root:
        if not root.left and not root.right:
            return 1 
        return countLeaves(root.left) + countLeaves(root.right)
    return 0

def countNodes(self, root):
        if root:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        return 0
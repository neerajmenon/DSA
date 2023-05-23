def isSubtree(self, root, subroot):
        if not subroot:
            return True
        if not root:
            return False

        if isSameTree(root, subroot):
            return True
        return isSubtree(root.left, subroot) or isSubtree(root.right, subroot)

def isSameTree(self, p,q):
    if p and q:
        l = isSameTree(p.left,q.left)
        r = isSameTree(p.right,q.right)
        vals = p.val == q.val
        return l and r and vals
    if p or q:
        return False
    return True
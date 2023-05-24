def ceil(root, inp):
 
    if root == None:
        return -1
    if root.key == inp:
        return root.key
    if root.key < inp:
        return ceil(root.right, inp)
    val = ceil(root.left, inp)
    return val if val >= inp else root.key

def Floor(root, inp):
 
    # Base Case
    if root == None:
        return -1
 
    # We found equal key
    if root.key == inp:
        return root.key
 
    # If root's key is larger, Floor must be in left subtree
    if root.key > inp:
        return Floor(root.left, inp)
 
    # Else, either right subtree or root has the Floor value
    else:
        floor = Floor(root.right, inp)
        # exception for -1 because it is being returned in base case
        return floor if floor <= inp and floor != -1 else root.key
    

# Two Sum BST
class Solution(object):
    def findTarget(self, root, k):
        s = set()
        def dfs(root):
            if root:
                if (k - root.val) in s:
                    return True
                s.add(root.val)
                return dfs(root.left) or dfs(root.right)
            return False
        return dfs(root)
    
# Range Sum of BST
class Solution:
    def rangeSumBST(self, root, low, high):
        sum = 0
        def dfs(root,l,r):
            nonlocal sum
            if root:
                if root.val >= l and root.val <= r:
                    sum+=root.val
                dfs(root.left,l,r)
                dfs(root.right,l,r)
        dfs(root,low,high)
        return sum
    
# BST to Greater Sum Tree (sum of all nodes greater than it)
class Solution:
    def bstToGst(self, root):
        self.sum = 0 

        def dfs(node):
            if node is None:
                return

            dfs(node.right) 
            self.sum += node.val
            node.val = self.sum
            dfs(node.left)

        dfs(root)

        return root

# BST to Smaller Sum Tree - Same thing in reverse
def addSmallerUtil(root, Sum):
     
    if root == None:
        return
 
    addSmallerUtil(root.left, Sum)
    Sum[0] = Sum[0] + root.key
    root.key = Sum[0]
    addSmallerUtil(root.right, Sum)
 
def addSmaller(root):
    Sum = [0]
    addSmallerUtil(root, Sum)
# 1 - Connect nodes at same level (level order traversal)
def connect(root):
 
    # Base condition
    if root is None:
        return
 
    # Create an empty queue like level order traversal
    queue = []
    queue.append(root)
    while len(queue) != 0:
 
        # size indicates no. of nodes at current level
        size = len(queue)
 
        # for keeping track of previous node
        prev = newnode(None)
        for i in range(size):
            temp = queue.pop(0)
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
            if prev != None:
                prev.nextRight = temp
                prev = temp
        prev.nextRight = None
        
        
# 2 - Binary Tree to DLL
class Solution:
    def bToDLL(self, root):
        prev = None

        def dfs(root):
            nonlocal prev
            if root:
                dfs(root.left)
                if prev is None:
                    prev = root
                else:
                    prev.right = root
                    root.left = prev
                    prev = root
                dfs(root.right)
                return root

        dfs(root)
        while prev.left:
            prev = prev.left

        return prev
       
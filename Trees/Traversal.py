# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 1 - INORDER
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
    
class Solution(object):
    def inorderTraversal(self, root):
        res = []
        stack = []
        
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        
        return res


#2 - PREORDER
class Solution(object):
    def preorderTraversal(self, root):
        arr = []
        def dfs(root):
            if root != None:
                arr.append(root.val)
                dfs(root.left)
                dfs(root.right)
        
        dfs(root)
        return arr
    

class Solution(object):
    def preorderTraversal(self, root):
        res = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        
        return res
    
# 3 - POSTORDER
class Solution(object):
    def postorderTraversal(self, root):
        res = []
        def dfs(root):
            if root:
                dfs(root.left)
                dfs(root.right)
                res.append(root.val)

        dfs(root)
        return res
    
class Solution(object):
    def postorderTraversal(self, root):
        res = []
        stack = [root]
        
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        
        return res[::-1]

# 4 - LEVEL ORDER
class Solution(object):
    def levelOrder(self, root):
 
        res = []
        queue = []
        if root:
            queue = [root]
        
        while queue:
            level = []
            level_size = len(queue)
            for i in range(level_size):
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        
        return res

# 5 - LEFT VIEW
def LeftView(root): # Modified Level Order
    
    q = []
    res = []
    if root:
        q = [root]
    while q:
        level = []
        level_size = len(q)
        for i in range(level_size):
            ele = q.pop(0) 
            if i == 0: # i == level_size-1 for right view
                res.append(ele.data)
            if ele.left:
                q.append(ele.left)
            if ele.right:
                q.append(ele.right)
    return res

def LeftView(root):
    res = []
    max_level = [0]
    def dfs(root,level,max_level):
        if root:
            if max_level[0] < level:
                res.append(root.data)
                max_level[0] = level
            dfs(root.left,level+1,max_level) # flip the order of these to get Right View
            dfs(root.right,level+1,max_level)
    dfs(root, 1, max_level)
    return res

# 6 - Find diff in sum btw nodes at odd/even levels. Flag Level Order pattern.
class Solution:
    def getLevelDiff(self, root):
        odd = 0
        even = 0
        q = []
        if root:
            q = [root]
        flag = True
        while q:
            l_size = len(q)
            for i in range(l_size):
                node = q.pop(0)
                if flag:
                    odd += node.data
                else:
                    even += node.data
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            flag = not flag
        return odd-even
    
    
# 7 - BOTTOM VIEW - tracking horizontal distances with hashmap
class Solution(object):
    def bottomView(self, root):
        res = []
        hm = {}
        q = []
        if root:
            q = [(root, 0)]
        
        while q:
            node, hd = q.pop(0)
            hm[hd] = node.data
            if node.left:
                q.append((node.left, hd - 1))
            if node.right:
                q.append((node.right, hd + 1))
                
        sorted_hds = sorted(hm.keys())
        res = [hm[hd] for hd in sorted_hds]
        
        return res

# 8 - MAXIMUM WIDTH
from collections import deque

class Solution:
    def widthOfBinaryTree(self, root):
        if not root:
            return 0
        
        max_width = 0
        queue = deque([(root, 0)])  # Queue to store nodes along with their indices
        
        while queue:
            level_width = len(queue)
            _, start_index = queue[0]  # Index of the leftmost node in the current level
            _, end_index = queue[-1]  # Index of the rightmost node in the current level
            max_width = max(max_width, end_index - start_index + 1)
            
            for _ in range(level_width):
                node, index = queue.popleft()
                if node.left:
                    queue.append((node.left, 2 * index))
                if node.right:
                    queue.append((node.right, 2 * index + 1))
        
        return max_width

    
# 9 - VERTICAL ORDER
from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # Dictionary to store nodes at each vertical level
        vertical_levels = defaultdict(list)

        # Helper function to perform DFS traversal and populate the vertical levels
        def dfs(node, level, depth):
            if node:
                heappush(vertical_levels[level], (depth, node.val))
                dfs(node.left, level - 1, depth + 1)
                dfs(node.right, level + 1, depth + 1)

        # Perform DFS traversal starting from the root
        dfs(root, 0, 0)

        # Sort the nodes in each vertical level based on depth and node values
        result = []
        for level in sorted(vertical_levels):
            nodes = []
            while vertical_levels[level]:
                nodes.append(heappop(vertical_levels[level])[1])
            result.append(nodes)

        return result


# 10 - ZIG ZAG LEVEL ORDER
class Solution:
    def zigzagLevelOrder(self, root):
        q = [] if not root else [root]
        res = []
        st = []
        flag = True # start with False if "Spiral Order"
        while q:
            l = [] 
            l_size = len(q)
            for i in range(l_size):
                node = q.pop(0)
                if flag:
                    l.append(node.val)
                else:
                    st.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if flag:
                res.append(l) # extend here if not want nested
            else:
                while st:
                    l.append(st.pop())
                res.append(l)
            flag = not flag
            
        return res
    

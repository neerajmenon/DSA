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
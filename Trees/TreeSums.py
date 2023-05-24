
#Given a binary tree, the task is to find the maximum path sum. 
#The path may start and end at ANY NODE in the tree.
class Solution:
    
    def findMaxSum(self, root):
        self.max_sum = float('-inf')

        def dfs(node):
            if node is None:
                return 0
            
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            # Calculate the maximum sum through the current node
            max_sum_through_node = max(node.data, node.data + left_sum, node.data + right_sum)

            # Calculate the maximum path sum if it goes through the current node
            max_path_sum = max(max_sum_through_node, node.data + left_sum + right_sum)

            # Update the maximum sum
            self.max_sum = max(self.max_sum, max_path_sum)

            # Return the maximum sum through the current node (excluding the current node)
            return max_sum_through_node

        dfs(root)
        return self.max_sum

# 3 - Max Path between TWO LEAVES
class Solution:
    def findMaxPathSum(self, root):
        self.max_path_sum = float('-inf')

        def dfs(node):
            if node is None:
                return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            # Update the maximum path sum if both children exist
            if node.left and node.right:
                max_path_sum = left_sum + right_sum + node.data
                self.max_path_sum = max(self.max_path_sum, max_path_sum)

            # Return the maximum sum through the current node (excluding the current node)
            if node.left:
                return left_sum + node.data
            elif node.right:
                return right_sum + node.data
            else:
                return node.data

        dfs(root)
        return self.max_path_sum

# 4 - Max Sum on a root to leaf path
class Solution:
    def maxLeafPathSum(self, root):
        maxsum = float("-inf")
        def dfs(root,sum):
            nonlocal maxsum
            if root:
                sum+=root.data
                if not root.left and not root.right:
                    maxsum = max(sum,maxsum)
                    return
                dfs(root.left,sum)
                dfs(root.right,sum)
        
        dfs(root,0)
        return maxsum
    
# 5 - Get all paths with target sum
class Solution:
    def printPathsWithSum(self, root, sum):
        res = []
        path = []
        def dfs(root,sum):
            if root:
                sum-=root.data
                path.append(root.data)
                if sum == 0:
                    res.append(path[:])
                dfs(root.left,sum)
                dfs(root.right,sum)
                path.pop()
            
        dfs(root,sum)
        return res
    
# 6- Is there a root to leaf path with target sum
class Solution(object):
    def hasPathSum(self, root, targetSum):

        if not root:
            return False

        targetSum -= root.val # reduce current node from sum
        
        if not root.left and not root.right: # if leaf, check sum
            return targetSum == 0

        return self.hasPathSum(root.left,targetSum) or self.hasPathSum(root.right,targetSum)

# 7- Transform node to hold its children's sum, but return up the node's sum. leaves reset to 0.
class Solution:
    def toSumTree(self, root) :
        if root:
            tmp = root.data
            root.data = self.toSumTree(root.left) + self.toSumTree(root.right)
            return tmp + root.data
        return 0
    
# 8 - Find # of good nodes, where good node has no prev node with val > it on path from root to it.
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, maxVal):
            if root:
                res = 1 if root.val >= maxVal else 0 # bigger than parent?
                maxVal = max(maxVal, root.val) # update
                res += dfs(root.left, maxVal) # add good from left
                res += dfs(root.right, maxVal) # add good from right
                return res # return total
            return 0

        return dfs(root, root.val)
class Solution(object):
   def lowestCommonAncestor(self, root, p, q):
        if (max(p.val, q.val) < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif (min(p.val, q.val) > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
        

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
    
class Solution(object):
    def kthSmallest(self, root, k):
        c = 0
        res = 0
        def dfs(root,k):
            nonlocal c
            nonlocal res
            if root:
                dfs(root.left,k)
                c+=1
                if c == k:
                    res = root.val
                    return
                dfs(root.right,k)
        dfs(root,k)

        return res
    
def kthLargest(root, k): # Go all the way right, then check lefts. -> decreasing nodes
    c = 0
    def dfs(root,k):
        nonlocal c
        if root == None or c >= k:
            return
    
        dfs(root.right, k, c)
        c+=1
        if c == k:
            print("K'th largest element is",root.key)
            return
    
        dfs(root.left, k, c)
        
        
class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return None

        mid = len(nums) // 2

        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedListToBST(self, head):
        if not head:
            return None
        
        mid = self.findMiddle(head)
        root = TreeNode(mid.val)
        
        # If there's only one node, no need to proceed further
        if head == mid:
            return root
        
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        
        return root
    
    def findMiddle(self, head):
        prev = None
        slow = head
        fast = head
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # Disconnect the left half from the middle node
        if prev:
            prev.next = None
        
        return slow

# DLL- https://www.geeksforgeeks.org/in-place-conversion-of-sorted-dll-to-balanced-bst/#


#-----Driver----

class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

def preOrder(root):
    if root == None:
        return
    print (root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)
    
class BinarySearchTree:
    def __init__(self): 
        self.root = None

#Node is defined as
#self.left (the left child of the node)
#self.right (the right child of the node)
#self.info (the value of the node)

    def insert(self, val):
        self.root = self._insert(self.root, val)
            

    def _insert(self, node, val):
        if node:
          if val < node.info:
            node.left = self._insert(node.left,val)
          elif val > node.info:
            node.right = self._insert(node.right,val)
          return node
        return Node(val)
        

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)

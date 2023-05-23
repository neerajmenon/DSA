#Iterative
class Solution(object):
    def isPalindrome(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        stack = []
        tmp = slow
        while slow:
            stack.append(slow.val)
            slow = slow.next
        
        curr = head
        while stack and curr:
            popped = stack.pop()
            if popped != curr.val:
                return False
            curr = curr.next
        
        return True
    
#Recursive
class Solution(object):
    def isPalindrome(self,head):
        def isPali(head):
            nonlocal end
            if head:
                v1 = isPali(head.next)
                v2 = end.val == head.val
                end = end.next
                return v1 and v2
            return True
        end = head
        return isPali(head)
            
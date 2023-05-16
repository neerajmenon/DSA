# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        
        st = []
        slow , fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        mid = slow

        while slow :
            st.append(slow)
            slow = slow.next
        
        res = head
        while res!=mid:
            temp = res.next
            res.next = st.pop()
            res.next.next = temp
            res = temp
        res.next = None
        return head
        
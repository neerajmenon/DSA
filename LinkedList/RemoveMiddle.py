#LC-2095 
#Delete middle node of a linked list

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        prev, slow, fast = head, head, head
        while fast!=None and fast.next!=None:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        if prev is not None:
            if prev.next is not None:
                prev.next = prev.next.next
            else:
                return None # 1 element case
        return head
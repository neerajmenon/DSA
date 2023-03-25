#LC-2095 
#Delete middle node of a linked list

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        if head.next == None:
            return None

        slow, fast = head, head.next.next
        while fast!=None and fast.next!=None:
            fast = fast.next.next
            slow = slow.next
        slow.next = slow.next.next

        return head
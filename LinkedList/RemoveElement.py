#LC-203 
#Remove element with given value from list
#https://stackoverflow.com/questions/3295938/else-clause-on-python-while-statement

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        prev = None
        curr = head
        while curr is not None:
            if curr.val is val:
                if prev is None:
                    head = curr.next
                else:
                    prev.next = curr.next       
            else:
                prev = curr
            curr = curr.next
               
        
        return head
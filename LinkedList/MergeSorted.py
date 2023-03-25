#LC-21
#Merge two sorted linked lists

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if list1 is None:
            return list2
        if list2 is None:
            return list1
            
        head = None
        if list1.val <= list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        
        curr = head
        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                curr.next = list1
                list1=list1.next
            else:
                curr.next = list2
                list2=list2.next
            curr = curr.next
        
        while list1 != None:
            curr.next = list1
            list1 = list1.next
            curr = curr.next
        
        while list2 != None:
            curr.next = list2
            list2 = list2.next
            curr = curr.next
        
        return head
        
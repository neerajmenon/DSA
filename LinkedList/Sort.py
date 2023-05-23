# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge_sort(self,head):
        if not head or not head.next:
            return head

        # Find the middle of the linked list
        slow, fast = head, head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second_half = slow.next
        slow.next = None

        # Recursively sort the two halves
        left = self.merge_sort(head)
        right = self.merge_sort(second_half)

        # Merge the sorted halves
        sorted_head = self.merge(left, right)

        return sorted_head


    def merge(self, left, right):
        dummy = ListNode(0)
        curr = dummy

        while left and right:
            if left.val <= right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next

        if left:
            curr.next = left
        if right:
            curr.next = right

        return dummy.next


    def sortList(self, head):
        if not head or not head.next:
            return head

        return self.merge_sort(head)
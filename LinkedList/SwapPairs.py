class Solution():
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        while current.next and current.next.next:
            node1 = current.next
            node2 = node1.next
            
            current.next = node2
            node1.next = node2.next
            node2.next = node1
            
            current = node1
        
        return dummy.next
    
# Recursive!
def swapPairs(head):
    if not head or not head.next:
        return head
    tmp = head.next
    head.next = swapPairs(head.next.next)
    tmp.next = head
    return tmp
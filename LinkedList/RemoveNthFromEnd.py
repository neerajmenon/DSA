class Solution(object):
    def removeNthFromEnd(self, head, k):
        p = head
        q = head
        prev = None
        count = 0
        
        while q and count < k:
            q = q.next
            count += 1
        
        if not q:
            return p.next  # head was the element
        
        while q:
            q = q.next
            prev = p
            p = p.next
        
        prev.next = p.next
        
        return head
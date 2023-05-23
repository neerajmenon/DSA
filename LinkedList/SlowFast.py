def hasCycle(self, head):
        slow,fast = head,head
        while fast!=None and fast.next!=None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
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
def hasCycle(self, head):
        slow,fast = head,head
        while fast!=None and fast.next!=None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
def removeMiddle(self, head):
        if head.next == None:
            return None

        slow, fast = head, head.next.next
        while fast!=None and fast.next!=None:
            fast = fast.next.next
            slow = slow.next
        slow.next = slow.next.next

        return head
    
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
    
def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
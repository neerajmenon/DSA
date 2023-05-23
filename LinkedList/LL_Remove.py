class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def removeNodeAtPosition(llist, position):
    head = llist
    idx = 0
    curr = head
    
    if position == 0:
      return head.next
    
    while curr and idx < position -1:
      curr = curr.next
      idx+=1
    curr.next = curr.next.next 
    return head

def removeNodeWithVal(self, head, val):
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
    
def removeDuplicates(self, head):
        curr = head
        while curr:
            if curr.next and curr.next.val == curr.val:
                curr.next = curr.next.next   
            else:
                curr = curr.next     
        return head
    
def removeAllDuplicates(self, head):
        dummy = ListNode(-1)  # Create a dummy node to handle the case where the head itself is a duplicate
        dummy.next = head

        prev = dummy
        curr = head

        while curr:
            if curr.next and curr.next.val == curr.val:
                # Skip all duplicate nodes
                while curr.next and curr.next.val == curr.val:
                    curr = curr.next

                prev.next = curr.next
            else:
                prev = curr

            curr = curr.next

        return dummy.next
    
def removeDuplicatesSet(head):
    if not head or not head.next:
        return head

    # Create a set to store unique values
    unique_values = set()
    unique_values.add(head.data)

    curr = head
    while curr.next:
        if curr.next.data in unique_values:
            # Skip the duplicate node
            curr.next = curr.next.next
        else:
            unique_values.add(curr.next.data)
            curr = curr.next

    return head

def removeAllDuplicatesSet(self, head):
        if not head or not head.next:
            return head

        unique_values = set()
        duplicates = set()

        curr = head
        while curr:
            if curr.val not in unique_values:
                unique_values.add(curr.val)
            else:
                duplicates.add(curr.val)

            curr = curr.next

        dummy = ListNode(-1)
        dummy.next = head

        prev = dummy
        curr = head

        while curr:
            if curr.val in duplicates:
                prev.next = curr.next
            else:
                prev = curr

            curr = curr.next

        return dummy.next

    
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
    
def removeMiddle(self, head):
        if head.next == None:
            return None

        slow, fast = head, head.next.next
        while fast!=None and fast.next!=None:
            fast = fast.next.next
            slow = slow.next
        slow.next = slow.next.next

        return head
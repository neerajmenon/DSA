def rotateRight(self, head, k):
        if not head:
            return head

        size = 1
        curr = head
        while curr.next:
            size+=1
            curr = curr.next
        
        k = k % size

        curr.next = head # last to first
        tmp = head
        for _ in range(size-k-1):
            tmp = tmp.next # reach breaking point
        
        head = tmp.next # head is the one after  breaking point
        tmp.next = None # reset breaking point's next to None

        return head 
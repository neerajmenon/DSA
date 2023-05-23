def sortList(head):
    if (head == None or 
        head.next == None):
        return head
  
    zeroD = Node(0)
    oneD = Node(0)
    twoD = Node(0)
    zero = zeroD 
    one = oneD 
    two = twoD
    
    curr = head
    while (curr):
        if (curr.data == 0):
            zero.next = curr
            zero = zero.next
            curr = curr.next
        elif(curr.data == 1):
            one.next = curr
            one = one.next
            curr = curr.next
        else:
            two.next = curr
            two = two.next
            curr = curr.next
          
    # Attach three lists
    zero.next = (oneD.next) if (oneD.next ) \
                            else (twoD.next)
    one.next = twoD.next
    two.next = None
    
    return zeroD.next
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def insertNodeAtTail(head, data):
  if not head:
    return Node(data)
  curr = head
  while curr.next:
    curr = curr.next
  curr.next = Node(data)
  return head

def insertNodeAtHead(head,data):
    if not head:
        return Node(data)
    tmp = Node(data)
    tmp.next = head
    head = tmp
    return head

def insertNodeAtPosition(llist, data, position):
    head = llist
    tmp = Node(data)
    if not head:
      return Node(data)
    if position == 0:
      tmp.next = head
      head = tmp
    
    curr = head
    idx = 0
    while curr and idx<position-1:
      curr = curr.next
      idx+=1
    
    tmp2 = curr.next
    curr.next = tmp
    tmp.next = tmp2
    return head
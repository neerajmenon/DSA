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


def sortedInsertSingleLL(head, data):
    new_node = Node(data)

    # Handle the case where the new node should be the new head
    if not head or data < head.data:
        new_node.next = head
        return new_node

    curr = head

    # Traverse the linked list to find the appropriate position to insert the new node
    while curr.next and curr.next.data < data:
        curr = curr.next

    new_node.next = curr.next
    curr.next = new_node

    return head


def sortedInsertDoubleLL(head, data):
    new_node = Node(data)
    
    if not head:
        return new_node
    
    if data < head.data:
        new_node.next = head
        head.prev = new_node
        return new_node
    
    curr = head
    
    while curr.next and curr.next.data < data:
        curr = curr.next
    
    new_node.prev = curr
    new_node.next = curr.next
    
    if curr.next:
        curr.next.prev = new_node
    curr.next = new_node
    
    return head
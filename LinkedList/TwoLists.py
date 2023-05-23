def compare_lists(p, q):
  while p and q:
    if p.data != q.data:
      return 0
    p = p.next
    q = q.next
    
  if not p and not q:
    return 1
  if not p or not q:
    return 0
  
"""
[List #1] a--->b--->c
                     \
                      x--->y--->z--->NULL
                     /
     [List #2] p--->q

"""

def findMergeNode(p, q):
  hs = set()
  while p:
    hs.add(p)
    p = p.next
  while q:
    if q in hs:
      return q.data
    q = q.next
  return -1


def mergeSortedLists(self, list1, list2):
        if list1 is None:
            return list2
        if list2 is None:
            return list1
            
        head = None
        if list1.val <= list2.val:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next
        
        curr = head
        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                curr.next = list1
                list1=list1.next
            else:
                curr.next = list2
                list2=list2.next
            curr = curr.next
        
        while list1 != None:
            curr.next = list1
            list1 = list1.next
            curr = curr.next
        
        while list2 != None:
            curr.next = list2
            list2 = list2.next
            curr = curr.next
        
        return head
    
def addTwoNumbers(self, l1,l2):
        dummy = ListNode()
        cur = dummy

        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            # update ptrs
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
def cookies(k, A):
    heapq.heapify(A)
    ops = 0
    while A and len(A) > 1 and A[0] < k:
      l1 = heapq.heappop(A)
      l2 = heapq.heappop(A)
      s = 1*l1 + 2*l2
      heapq.heappush(A,s)
      ops+=1
    
    return ops if A and A[0]>=k else -1
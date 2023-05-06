# https://www.geeksforgeeks.org/sde-sheet-a-complete-guide-for-sde-preparation/

# Leaders in Array (Greatest element when looking right)
def printLaders(arr, size):
    sk = []
    sk.append(arr[size - 1])
    for i in range(size - 2, -1, -1):
        if(arr[i] >= sk[len(sk) - 1]):
            sk.append(arr[i])
 
    while(len(sk) != 0):
        print(sk[len(sk)-1],end = ' ')
        sk.pop()
        
# Equilibrium Point - Element s.t. sum(LHS)=sum(RHS) 
def findElement(arr, size) :
    right_sum, left_sum = 0, 0
    for i in range(1, size) :
        right_sum += arr[i]
    i, j = 0, 1
    while j < size :
        right_sum -= arr[j]
        left_sum += arr[i]
        if left_sum == right_sum :
            return arr[i + 1]
        j += 1
        i += 1
 
    return -1
 
         
# Sort 0s,1s,2s - Pointer Method
def sort012(a, arr_size):
    lo = 0
    hi = arr_size - 1
    mid = 0
    while mid <= hi:
        if a[mid] == 0:
            a[lo], a[mid] = a[mid], a[lo]
            lo = lo + 1
            mid = mid + 1
        elif a[mid] == 1:
            mid = mid + 1
        else:
            a[mid], a[hi] = a[hi], a[mid]
            hi = hi - 1
    return a

# Reverse every sub-array of consecutive k elements
def reverse(arr, n, k):
    i = 0
    while(i<n):
        left = i
        right = min(i + k - 1, n - 1)
        while (left < right):
            arr[left], arr[right] = arr[right], arr[left]
            left+= 1
            right-=1
        i+= k
        
# Sort in zig-zag fashion
def zigZag(arr, n):
    arr.sort()
    for i in range(1, n-1, 2):
        arr[i], arr[i+1] = arr[i+1], arr[i]
    print(arr)
    
# Subarray Sum
def subarraySum(self, nums, k):
    d = {}
    d[0] = 1
    s = 0
    count = 0
    for i in range(len(nums)):
        s += nums[i]
        if s-k in d:
            count += d[s-k]
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    
    return count
import heapq

def heap_sort(arr):
    # Convert the input list to a heap
    heapq.heapify(arr)

    # Create an empty result list
    sorted_arr = []

    # Pop elements from the heap and append them to the result list
    while arr:
        sorted_arr.append(heapq.heappop(arr))

    return sorted_arr

# Usage example
arr = [12, 11, 13, 5, 6, 7]
sorted_arr = heap_sort(arr)
print("Sorted array:", sorted_arr)

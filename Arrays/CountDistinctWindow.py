from collections import defaultdict

def count_distinct_elements(arr, k):
    distinct_counts = []
    window_counts = defaultdict(int)
    distinct_count = 0

    # Count the frequencies of elements in the first window
    for i in range(k):
        if window_counts[arr[i]] == 0:
            distinct_count += 1
        window_counts[arr[i]] += 1

    distinct_counts.append(distinct_count)

    # Slide the window through the array
    for i in range(k, len(arr)):
        left_elem = arr[i - k]

        # Remove the leftmost element from the window
        window_counts[left_elem] -= 1
        if window_counts[left_elem] == 0:
            distinct_count -= 1

        right_elem = arr[i]

        # Add the rightmost element to the window
        if window_counts[right_elem] == 0:
            distinct_count += 1
        window_counts[right_elem] += 1

        distinct_counts.append(distinct_count)

    return distinct_counts

# Example usage:
arr = [1, 2, 1, 3, 4, 2, 3]
k = 3
result = count_distinct_elements(arr, k)
print(result)

def find_top_k_numbers(arr, k):
    frequency_dict = {}
    for num in arr:
        if num in frequency_dict:
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1
    
    top_k_numbers = []
    for _ in range(k):
        max_num = None
        max_freq = -1
        for num, freq in frequency_dict.items():
            if freq > max_freq or (freq == max_freq and num > max_num):
                max_num = num
                max_freq = freq
        if max_num is not None:
            top_k_numbers.append(max_num)
            del frequency_dict[max_num]
    
    return top_k_numbers

def find_top_k_numbers(arr, k):
    frequency_dict = {}
    for num in arr:
        if num in frequency_dict:
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1
    
    top_k = sorted(frequency_dict.items(), key=lambda x: (-x[1], -x[0]))
    top_k_numbers = []
    for i in range(k):
        top_k_numbers.append(top_k[i][0])
    return top_k_numbers

# Example usage:
arr = [4, 5, 2, 4, 1, 3, 2, 5, 4]
k = 3
result = find_top_k_numbers(arr, k)
print(result)

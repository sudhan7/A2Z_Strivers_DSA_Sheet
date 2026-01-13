def longest_subarray_negatives(arr, k):
    max_len = 0
    n = len(arr)
    sums = 0
    freq = {}
    for i in range(n):
        sums+=arr[i]

        if sums == k:
            max_len = i+1
        
        rem = sums-k
        if rem in freq:
            max_len = max(max_len,i-freq[rem])
        
        if sums not in freq:
            freq[sums] = i
    return max_len

arr = [-1, 1, 1]
k = 1  
print(longest_subarray_negatives(arr, k))
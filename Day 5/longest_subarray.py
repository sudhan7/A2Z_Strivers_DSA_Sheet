def longest_subarray(arr, k):
    max_len = 0
    i=0
    j=0
    n = len(arr)
    sums = arr[0]
    while j<n:
        while i<=j and sums>k:
            sums-=arr[i]
            i+=1
        if sums == k:
            max_len = max(max_len, j-i+1)
        j+=1
        if j<n:
            sums+=arr[j]
    return max_len
arr = [10, 5, 2, 7, 1, 9]
k = 15  
print(longest_subarray(arr,k))
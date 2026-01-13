def maximum_subarray(arr):
    max_len = float('-inf')
    count = 0
    for i in range(len(arr)):
        count += arr[i]

        if count > max_len:
            max_len = count
            
        if count < 0:
            count = 0
    
    return max_len

arr =[-2, -3, -7, -2, -10, -4]  
print(maximum_subarray(arr))
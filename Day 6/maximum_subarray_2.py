def maximum_subarray_2(arr):
    max_len = float('-inf')
    count = 0
    start = 0
    ansStart = -1
    ansEnd = -1
    for i in range(len(arr)):
        if count == 0:
            start = i
        count += arr[i]

        if count > max_len:
            max_len = count
            ansStart = start
            ansEnd = i
            
        if count < 0:
            count = 0
    
    return arr[ansStart:ansEnd+1]

arr = [-2, -3, -7, -2, -10, -4]    
print(maximum_subarray_2(arr))
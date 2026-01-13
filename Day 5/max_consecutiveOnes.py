def max_consecutiveOnes(arr):
    max_len = 0
    counter = 0

    for num in arr:
        if num == 1:
            counter +=1
            max_len = max(max_len,counter)
        else:
            counter = 0
    return max_len

arr = [1, 1, 0, 1, 1, 1]
print(max_consecutiveOnes(arr))
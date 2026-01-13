def leftRotate_arrayByOne(arr):
    temp = arr[0]
    n = len(arr)
    for i in range(n-1):
        arr[i] = arr[i+1]
    
    arr[n-1] = temp

    return arr

arr = [-1, 0, 3, 6]  
print(leftRotate_arrayByOne(arr))
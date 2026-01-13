def recursive_bubblesort(arr):
    n = len(arr)

    sort = True

    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            sort = False

    if sort == False:
        recursive_bubblesort(arr)
        
    return arr

arr = [4,7,8,1,1,3,44,5,7]
print(recursive_bubblesort(arr))
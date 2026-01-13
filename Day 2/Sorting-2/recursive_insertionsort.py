def recursive_insertionsort(arr,i,n):
    if i == n:
        return
    
    j = i

    while j > 0 and arr[j-1] > arr[j]:
        arr[j], arr[j-1] = arr[j-1], arr[j]
        j-=1

    recursive_insertionsort(arr,i+1,n)

    return arr

arr = [13, 46, 24, 52, 20, 9]
print(recursive_insertionsort(arr,0,len(arr)))
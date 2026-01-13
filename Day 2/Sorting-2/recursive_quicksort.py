def recursive_quicksort(arr,low,high):
    if low < high:
        partition_pos = partition(arr,low,high)
        recursive_quicksort(arr,low,partition_pos-1)
        recursive_quicksort(arr,partition_pos+1,high)
    return arr

def partition(arr,low,high):
    pivot = arr[low]
    i = low
    j = high

    while i<j:
        while arr[i] <= pivot and i <= high - 1:
            i+=1
        while arr[j] > pivot and j >= low + 1:
            j-=1
    
    if i < j:
        arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]
    return j

arr = [13, 46, 24, 52, 20, 9]
print(recursive_quicksort(arr,0,len(arr)-1))

def minimum_in_rotated_sorted_array(arr):
    n = len(arr)
    low = 0
    high = n-1
    mini = float('inf')
    
    while low <= high:
        mid = (low+high)//2
        if arr[low] <= arr[high]:
            mini = min(mini,arr[low])
            break
        if arr[low] <= arr[mid]:
            mini = min(mini,arr[low])
            low = mid+1
        else:
            mini = min(arr[mid],mini)
            high = mid-1
    return mini       

arr = [1,2]
print(minimum_in_rotated_sorted_array(arr))
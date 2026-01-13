def rotated_sorted_arr(arr,k):
    n = len(arr)
    low = 0 
    high = n-1
    while low<=high:
        mid = (low+high)//2
        if arr[mid] == k:
            return mid
        if arr[low] <= arr[mid]:
            if arr[low] <= k and k <= arr[mid]:
                high = mid-1
            else:
                low = mid+1
        else:
            if arr[mid] <= k and k <= arr[high]:
                low = mid+1
            else:
                high = mid-1
    return -1


arr = [4, 5, 6, 7, 0, 1, 2]
k = 7
print(rotated_sorted_arr(arr,k))
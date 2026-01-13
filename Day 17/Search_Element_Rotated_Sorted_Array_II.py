def Search_Element_Rotated_Sorted_Array_II(arr,k):
    n = len(arr)
    low = 0
    high = n-1

    while low<=high:
        mid = (low+high)//2
        if arr[mid] == k:
            return True
        if arr[low] == arr[mid] == arr[high]:
            low += 1
            high -=1
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
    return False

arr = [3, 1, 2, 3, 3, 3, 3]
k = 1
print(Search_Element_Rotated_Sorted_Array_II(arr,k))
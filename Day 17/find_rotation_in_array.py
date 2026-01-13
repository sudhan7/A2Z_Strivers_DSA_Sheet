def find_rotation_in_array(arr):
    n = len(arr)
    low = 0
    high = n-1
    mini = float('inf')
    index = -1
    
    while low <= high:
        mid = (low+high)//2
        if arr[low] <= arr[high]:
            if arr[low] < mini:
                mini = arr[low]
                index = low
            break
        if arr[low] <= arr[mid]:
            if arr[low] < mini:
                mini = arr[low]
                index = low
            low = mid+1
        else:
            if arr[mid] < mini:
                mini = arr[mid]
                index = mid
            high = mid-1
    return index        

arr = [4,5,6,7,0,1,2,3]
print(find_rotation_in_array(arr))
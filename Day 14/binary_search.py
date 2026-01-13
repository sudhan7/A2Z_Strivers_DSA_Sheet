def binary_search(arr,low,high,target):
    if low > high:
        return -1
    mid = (low+high)//2

    if arr[mid] == target:
        return mid
    elif target > arr[mid]:
        return binary_search(arr,mid+1,high,target)
    else:
        return binary_search(arr,low,mid-1,target)

def search(arr,target):
    n = len(arr)
    return binary_search(arr,0,n-1,target)


arr = [3,4,7,10,12,16]
target = 16
print(search(arr,target))

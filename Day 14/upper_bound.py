def upper_bound(arr,x):
    n = len(arr)
    low = 0
    high = n-1
    ans = n

    while low <= high:
        mid = (low+high)//2
        if arr[mid] > x:
            ans = mid
            high = mid-1
        else:
            low = mid+1
    return ans 

arr = [1,2,2,3]
x = 2
print(upper_bound(arr,x))
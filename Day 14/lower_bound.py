def lower_bound(arr,x):
    n = len(arr)
    low = 0
    high = n-1
    ans = n

    while low <= high:
        mid = (low+high)//2
        if arr[mid] >= x:
            ans = mid
            high = mid-1
        else:
            low = mid+1
    return ans 

arr = [10,20,30,40,50]
x = 25
print(lower_bound(arr,x))
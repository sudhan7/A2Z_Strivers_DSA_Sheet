def numDays(arr,mid):
    days = 1
    load = 0
    for num in arr:
        if num + load > mid:
            days+=1
            load = num
        else:
            load+=num
    return days

def Capacity_Ship_Packages(arr,d):
    low = max(arr)
    high = sum(arr)

    while low <= high:
        mid = (low+high)//2
        days = numDays(arr,mid)

        if days <= d:
            high = mid-1
        else:
            low = mid+1
    return low

arr = [1, 2, 3, 4, 5]
d = 2
print(Capacity_Ship_Packages(arr,d))
def first_occurence(arr,n,k):
    low = 0
    high = n-1
    first = -1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == k:
            first = mid
            high = mid-1
        elif arr[mid] < k:
            low = mid+1
        else:
            high = mid-1
    return first

def last_occurence(arr,n,k):
    low = 0
    high = n-1
    last = -1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == k:
            last = mid
            low = mid+1
        elif arr[mid] < k:
            low = mid+1
        else:
            high = mid-1
    return last



def first_last_occurence(arr,n,k):
    first = first_occurence(arr,n,k)
    if first == -1:
        return [-1,-1]
    last = last_occurence(arr,n,k)
    return [first,last]

arr = [3, 4, 13, 13, 13, 20, 40]
n = 7
k = 13
print(first_last_occurence(arr,n,k))
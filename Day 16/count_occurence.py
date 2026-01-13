def first_occurence(arr,n,k):
    low = 0 
    high = n-1
    first = -1

    while low <= high:
        mid = (low+high)//2
        if arr[mid] == x:
            first = mid
            high = mid-1
        elif arr[mid] < x:
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
        if arr[mid] == x:
            last = mid
            low = mid+1
        elif arr[mid] < x:
            low = mid+1
        else:
            high = mid-1
    return last
def count_occurence(arr,n,x):
    first = first_occurence(arr,n,x)
    if first == -1:
        return 0
    last = last_occurence(arr,n,x)
    return last-first+1


n = 8
x= 2
arr = [1, 1, 2, 2, 2, 2, 2, 3]
print(count_occurence(arr,n,x))
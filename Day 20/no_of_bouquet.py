def possible(arr,day,m,k):
    count = 0
    no_of_bouqutes = 0

    for num in arr:
        if num <= day:
            count += 1
            if count == k:
                no_of_bouqutes += count/k
                count = 0
        else:
            count = 0
    return no_of_bouqutes >= m
    

def no_of_bouquet(n,arr,m,k):
    low = min(arr)
    high = max(arr)
    ans = -1

    while low <= high:
        mid = (low+high)//2

        if possible(arr,mid,m,k):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

n = 5
arr = [1, 10, 3, 10, 2]
m = 3
k = 2
print(no_of_bouquet(n,arr,m,k))
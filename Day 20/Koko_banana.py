import math
def find_totalHour(arr,speed):
    total = 0
    for num in arr:
        total += math.ceil(num/speed)
    return total

def koko_banana(n,h,arr):
    maxPile = max(arr)
    low = 1
    high = maxPile
    ans = maxPile

    while low<= high:
        mid = (low+high)//2
        totalHour = find_totalHour(arr,mid)

        if totalHour <= h:
            ans = mid
            high = mid-1
        else:
            low = mid+1
    return ans

n = 4
arr = [7, 15, 6, 3]
h = 8
print(koko_banana(n,h,arr))
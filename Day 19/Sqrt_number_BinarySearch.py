def Sqrt_number_BinarySearch(n):
    low = 1
    high = n
    while low <= high:
        mid = (low+high)//2
        val = mid * mid
        if val <= n:
            low = mid+1
        else:
            high = mid-1
    return high

n = 28
print(Sqrt_number_BinarySearch(n))
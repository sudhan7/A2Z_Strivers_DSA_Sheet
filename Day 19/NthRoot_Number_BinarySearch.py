def NthRoot_Number_BinarySearch(n, m):
    low = 1
    high = m

    while low <= high:
        mid = (low+high)//2
        ans = 1
        for _ in range(n):
            ans *= mid
            if ans > m:
                break
        
        if ans == m:
            return mid
        
        if ans < m:
            low = mid+1
        else:
            high = mid-1
    return -1

n = 4
m = 69
print(NthRoot_Number_BinarySearch(n,m))
import math
def cal_sum(arr,val,n):
    sum = 0
    for i in range(n):
        sum += math.ceil(arr[i]/val)
    return sum

def Smallest_Divisor_Threshold(arr,limit,n):
    low = min(arr)
    high = max(arr)
    ans = -1

    while low <= high:
        mid = (low+high)//2
        sum = cal_sum(arr,mid,n)
        if sum <= limit:
            ans = mid
            high = mid-1
        else:
            low = mid + 1
    return ans


n = 4 
arr = [8,4,2,3] 
limit = 10
print(Smallest_Divisor_Threshold(arr,limit,n))
def countSubarray_sumEqualsK(arr,n,k):
    res = {}
    res[0] = 1
    count = 0
    prefSum = 0

    for i in range(n):
        prefSum+=arr[i]
        remove = prefSum - k
        if remove in res:
            count += res[remove]
        
        res[prefSum] = res.get(prefSum,0)+1


    return count

n = 3
arr = [1,2,3] 
k = 3
print(countSubarray_sumEqualsK(arr,n,k))

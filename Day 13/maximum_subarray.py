# def maximum_subarray(arr):
#     n = len(arr)
#     maxi = float('-inf')
#     for i in range(n):
#         temp = 1
#         for j in range(i,n):
#             temp*=arr[j]
#             maxi = max(maxi,temp)
#     return maxi

def maximum_subarray(arr):
    n = len(arr)
    ans = float('-inf')
    prefix = 1 
    suffix = 1

    for i in range(n):
        if prefix == 0:
            prefix = 1
        if suffix == 0:
            suffix = 1

        prefix *= arr[i]
        suffix *= arr[n-i-1]

        ans = max(ans, max(prefix,suffix))
    return ans 



arr = [1,2,3,4,5,0]
print(maximum_subarray(arr))

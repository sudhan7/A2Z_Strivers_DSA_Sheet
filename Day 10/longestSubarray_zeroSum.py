# def longestSubarray_zeroSum(arr,n):
#     max_count = 0
#     zero_sum = float('-inf')
#     for i in range(n):
#         zero_sum = arr[i]
#         for j in range(i+1,n):
#             zero_sum+=arr[j]
#             if zero_sum == 0:
#                 max_count = max(max_count,j-i+1)
#     return max_count

def longestSubarray_zeroSum(arr,n):
    maxi = 0
    sum = 0
    hashmap = {}
    
    for i in range(n):
        sum+=arr[i]
        if sum == 0:
            maxi = i+1
        elif sum in hashmap.keys():
            temp = i - hashmap[sum]
            maxi = max(maxi,temp)
        else:
            hashmap[sum] = i
    return maxi


arr = [9, -3, 3, -1, 6, -5]
n = 6
print(longestSubarray_zeroSum(arr,n))
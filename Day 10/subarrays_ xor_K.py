# def subarrays_xor_K(arr, k):
#     count = 0
#     for i in range(len(arr)):
#         xor = 0
#         for j in range(i,len(arr)):
#             xor ^= arr[j]
#             if xor == k:
#                 count+=1
#     return count
def subarrays_xor_K(arr, k):
    count = 0
    freq = {}
    freq[0] = 1
    prefixXor = 0
    for num in arr:
        prefixXor ^= num
        target = prefixXor ^ k
        if target in freq:
            count+=freq[target]
        freq[prefixXor] = freq.get(prefixXor,0) + 1
    return count

arr = [4, 2, 2, 6, 4]
k = 6
print(subarrays_xor_K(arr,k))
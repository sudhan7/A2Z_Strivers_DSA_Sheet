# def max_consecutive_ones(arr,k):
#     left = 0
#     zeros = 0
#     max_len = 0
#     for right in range(len(arr)):
#         if arr[right] == 0:
#             zeros+=1

#         while zeros > k:
#             if arr[left] == 0:
#                 zeros-=1
#             left += 1
        
#         max_len = max(max_len, right-left+1)
#     return max_len

def max_consecutive_ones(arr,k):
    left = 0
    zeros = 0
    max_len = 0

    for right in range(len(nums)):
        if arr[right] == 0:
            zeros+=1
        
        if zeros > k:
            if arr[left] == 0:
                zeros -= 1
            left+=1
        
        
        max_len = max(max_len, right-left+1)
        
    return max_len
        

nums = [0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1] 
k = 3
print(max_consecutive_ones(nums,k))
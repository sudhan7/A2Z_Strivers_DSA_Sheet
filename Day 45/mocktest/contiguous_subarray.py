def contiguous_subarray(arr):
    left = 0 
    max_len = 0
    max_sum = 0
    curr_sum = 0

    for right in range(len(arr)):
        curr_sum += arr[right]
        while curr_sum > k:
            curr_sum -= arr[left]
            left+=1
        max_sum = max(max_sum,curr_sum)
        if curr_sum >= max_sum:
            max_len = max(max_len,right-left+1)
    return max_len
        

nums = [1, 2, 1, 0, 1, 1, 0]
k = 4
print(contiguous_subarray(nums))

'''
Return the length of the longest contiguous subarray such that
the sum of the subarray is at most k.

Input:
nums = [1, 2, 1, 0, 1, 1, 0]
k = 4

Output:
4

Explanation:
The subarray [1, 0, 1, 1, 0] has sum 3 and length 5,
but the longest valid subarray with sum ≤ 4 is [2,1,0,1] → length 4

'''
def helper(ind,sum,nums):
    if sum == 0:
        return 1
    
    if sum < 0 or ind == len(nums):
        return 0
    
    return helper(ind+1, sum - nums[ind], nums) + helper(ind+1, sum, nums)

def subsequences_sumK(nums,k):
    return helper(0,k,nums)

nums = [4, 9, 2, 5, 1] 
k = 10
print(subsequences_sumK(nums,k))
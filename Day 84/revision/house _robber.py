def house_robber(nums):
    return helper(0,nums)

def helper(i, nums):
    if i>=len(nums):
        return 0
    
    rob = nums[i] + helper(i+2,nums)
    skip = helper(i+1,nums)

    return max(rob,skip)

nums = [2,1,1,2]
print(house_robber(nums))
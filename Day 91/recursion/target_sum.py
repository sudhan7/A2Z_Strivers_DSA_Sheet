def findTargetSumWays(nums, target):
    def ways(i, current_sum):
        #base case
        if i == len(nums):
            return 1 if current_sum == target else 0
        
        # choice 1?
        add = ways(i+1, current_sum+nums[i])
        
        # choice 2?
        subract = ways(i+1, current_sum-nums[i])
        
        # combine?
        return add+subract
    
    return ways(0, 0)

nums = [1,1,1,1,1]
target = 3
print(findTargetSumWays(nums,target))

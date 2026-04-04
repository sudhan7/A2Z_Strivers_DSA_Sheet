def three_sum(nums):
    nums.sort()
    res = []
    for i in range(len(nums)-1):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l = i+1
        r = len(nums)-1

        while l<r:
            target = nums[i] + nums[l] + nums[r]
            if target == 0:
                res.append([nums[i] ,nums[l], nums[r]])
                l+=1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
            if target < 0:
                l+=1
            else:
                r-=1
    return res



nums = [-1,0,1,2,-1,-4]
print(three_sum(nums))
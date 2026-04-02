def target_sum(nums, target):
    l,r = 0, len(nums)-1
    while l<r:
        ans = nums[l] + nums[r]
        if ans == target:
            return [l+1, r+1]
        elif ans > target:
            r-=1
        else:
            l+=1
    return

numbers = [1,2,3,4]
target = 3
print(target_sum(numbers, target))
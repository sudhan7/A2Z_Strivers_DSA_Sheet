def max_consecutive_ones(nums):
    left = 0
    right = 0
    ans = 0
    n = len(nums)-1

    while right <= n:
        if nums[right] == 0:
            ans = max(ans, right-left)
            while right <= n and nums[right] == 0:
                right += 1
            left = right
        else:
            right += 1
    return max(ans, right - left)

nums = [1,1,0,1,1,1]
print(max_consecutive_ones(nums))
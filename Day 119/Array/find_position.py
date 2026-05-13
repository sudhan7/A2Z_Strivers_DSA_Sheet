def find_pos(arr,target):
    l,r = 0, len(nums)-1

    while l<=r:
        m = (l+r)//2

        if target == nums[m]:
            return m
        elif target < nums[m]:
            r = m-1
        else:
            l = m+1
    return l

nums = [1,3,5,6]
target = 7
print(find_pos(nums,target))
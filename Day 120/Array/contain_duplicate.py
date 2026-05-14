def containsNearbyDuplicate(nums,k):
    mpp = {}

    for i in range(len(nums)):
        if nums[i] in mpp:
            if i - mpp[nums[i]] <= k:
                return True
        mpp[nums[i]] = i
    return False

nums = [1,2,3,1]
k = 3
print(containsNearbyDuplicate(nums,k))
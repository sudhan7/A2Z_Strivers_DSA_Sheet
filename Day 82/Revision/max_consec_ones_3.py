def longestOnes(nums, k):
    temp = 0
    left = 0
    ans = 0

    n = len(nums)
    
    for right,n in enumerate(nums):
        if n == 0:
            temp += 1

        while temp > k:
            if nums[left] == 0:
                temp -= 1
            left+=1
        
        ans = max(ans, right - left + 1)
    return ans

            


nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1] 
k = 3
print(longestOnes(nums, k))
def smallerNumbersThanCurrent(nums):
    sorted_nums = sorted(nums)
    dic = {}
    ans = []

    for i,v in enumerate(sorted_nums):
        if v not in dic:
            dic[v] = i
    
    for i in nums:
        ans.append(dic[i])
    
    return ans


nums = [8,1,2,2,3]
print(smallerNumbersThanCurrent(nums))
def findCombinations(n,last,nums,k,ans):
    if n == 0 and len(nums) == k:
        ans.append(list(nums))
        return
    
    if n <= 0 or len(nums) > k:
        return
    
    for i in range(last,10):
        if i <= n:
            nums.append(i)
            findCombinations(n-i,i+1,nums,k,ans)
            nums.pop()
        else:
            break
    


def combinationSum3(n,k):
    nums = []
    ans = []
    findCombinations(n,1,nums,k,ans)
    return list(ans)


k = 3 
n = 9
print(combinationSum3(n,k))
def finCombination(ind,target,arr,ans,ds):
    #base case
    if ind == len(arr):
        if target == 0:
            ans.append(list(ds))
        return
    
    if arr[ind] <= target:
        ds.append(arr[ind])
        finCombination(ind,target-arr[ind],arr,ans,ds)
        ds.pop()
    finCombination(ind+1,target,arr,ans,ds)

def combinationSum(v,target):
    ans = []
    ds = []
    finCombination(0,target,v,ans,ds)
    return ans

v = [2, 3, 6, 7]  
target = 7  
print(combinationSum(v,target))
def findCombination(ind,arr,k,ans,ds):
    if ind == len(arr):
        if k == 0:
            ans.append(list(ds))
        return
    
    if arr[ind] <= k:
        ds.append(arr[ind])
        findCombination(ind+1,arr,k-arr[ind],ans,ds)
        ds.pop()
    findCombination(ind+1,arr,k,ans,ds)

def combinationSum2(arr,k):
    arr.sort()
    ans = []
    ds = []
    findCombination(0,arr,k,ans,ds)
    return ans

candidates = [10,1,2,7,6,1,5]
target = 8
print(combinationSum2(candidates,target))
def findCombination(ind,arr,ans,ds):
    ans.append(list(ds))
    for i in range(ind,len(arr)):
        if i > ind and arr[i] == arr[i-1]:
            continue
        ds.append(arr[i])
        findCombination(i+1,arr,ans,ds)
        ds.pop()

def subset2(arr):
    arr.sort()
    ans = []
    ds = []
    findCombination(0,arr,ans,ds)
    return ans

arr = [1,2,2]
print(subset2(arr))
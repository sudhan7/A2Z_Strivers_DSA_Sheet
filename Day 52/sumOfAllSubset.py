def findSubset(ind,arr,n,ds,ans):
    if ind == n:
        ans.append(ds)
        return
    
    findSubset(ind+1,arr,n,ds+arr[ind],ans)
       
    findSubset(ind+1,arr,n,ds,ans)

def sumOfAllSubset(arr,n):
    arr.sort()
    ds = 0
    ans = []
    findSubset(0,arr,n,ds,ans)
    return sorted(ans)

n = 3 
arr = [5,2,1]
print(sumOfAllSubset(arr,n))
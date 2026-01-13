def four_sum(arr,target):
    arr.sort()
    n = len(arr)
    ans = []

    for i in range(n):
        if i>0 and arr[i] == arr[i-1]:
            continue
        for j in range(i+1,n):
            if j>i+1 and arr[j] == arr[j-1]:
                continue
            k = j+1
            l = n-1
            while(k<l):
                total = arr[i]+arr[j]+arr[k]+arr[l]
                if total == target:
                    ans.append([arr[i], arr[j] ,arr[k] ,arr[l]])
                    while k<l and arr[k] == arr[k+1]:
                        k+=1
                    while k<l and arr[l] == arr[l-1]:
                        l-=1
                    k+=1
                    l-=1
                elif total < target:
                    k+=1
                else:
                    l-=1
    return ans

arr = [4,3,3,4,4,2,1,2,1,1]
target = 9
print(four_sum(arr,target))
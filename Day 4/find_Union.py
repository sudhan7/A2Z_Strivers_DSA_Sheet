def find_Union(arr1, arr2, n, m):
    union = []
    i,j=0,0

    while i<n and j<m:
        if arr1[i] < arr2[j]:
            if not union or union[-1] != arr1[i]:
                union.append(arr1[i])
            i+=1
        elif arr2[j] < arr1[i]:
            if not union or union[-1] != arr2[j]:
                union.append(arr2[j])
            j+=1
        else:
            if not union or union[-1] != arr2[j]:
                union.append(arr2[j])
            i+=1
            j+=1
    
    while i<n:
        if not union or union[i] != arr1[i]:
            union.append(arr1[i])
        i+=1

    while j<m:
        if not union or union[j] != arr2[j]:
            union.append(arr2[j])
        j+=1
    return union


n = 5
m = 5 
arr1= [1,2,3,4,5]  
arr2 = [2,3,4,4,5]
print(find_Union(arr1, arr2, n, m))
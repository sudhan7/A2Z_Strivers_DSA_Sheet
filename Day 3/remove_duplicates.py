# def remove_duplicates(arr):
#     return list(set(arr))

def remove_duplicates(arr):
    i = 0
    for j in range(1,len(arr)):
        if arr[j] != arr[i]:
            arr[i+1] = arr[j]
            i+=1
    return arr[:i+1]
     

arr = [1,1,2,2,2,3,3]
print(remove_duplicates(arr))
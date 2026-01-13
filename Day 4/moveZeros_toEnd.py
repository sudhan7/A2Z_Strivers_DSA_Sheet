def moveZeros_toEnd(arr):
    i=0
    j=len(arr)-1
    while(i<j):
        if arr[i] == 0 and arr[j]!=0:
            arr[i],arr[j] = arr[j],arr[i]
            i+=1
            j-=1
        elif arr[i] != 0:
            i+=1
        else:
            j-=1
    return arr

arr = [1,2,0,1,0,4,0]
print(moveZeros_toEnd(arr))
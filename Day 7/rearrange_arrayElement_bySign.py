# def rearrange_element(arr, n):
#     pos = []
#     neg = []
#     res = []

#     for num in arr:
#         if num < 0:
#             neg.append(num)
#         else:
#             pos.append(num)
    
#     i=0

#     while i<n//2:
#         res.append(pos[i])
#         res.append(neg[i])
#         i+=1
    
#     return res

def rearrange_element(arr, n):
    res = [0]*n
    posInd = 0
    negInd = 1

    for i in range(len(arr)):
        if arr[i] < 0:
            res[negInd] = arr[i]
            negInd+=2
        else:
            res[posInd] = arr[i]
            posInd+=2
    
    return res

arr = [1,2,-3,-1,-2,3]
n = 6
print(rearrange_element(arr,n))

def rearrange_element_variety2(arr, n):
    pos = []
    neg = []

    for num in arr:
        if num < 0:
            neg.append(num)
        else:
            pos.append(num)
    
    if len(pos) > len(neg):
        for i in range(len(neg)):
            arr[2*i] = pos[i]
            arr[2*i+1] = neg[i]

        index = len(neg) * 2
        for i in range(len(neg),len(pos)):
            arr[index] = pos[i]
            index+=1
    else:
        for i in range(len(pos)):
            arr[2*i] = pos[i]
            arr[2*i+1] = neg[i]

        index = len(pos) * 2
        for i in range(len(pos),len(neg)):
            arr[index] = neg[i]
            index+=1
    return arr

arr = [-1,2,3,4,-3,1] #[2,-1,3,-3,4,1]
n = 6
print(rearrange_element_variety2(arr,n))
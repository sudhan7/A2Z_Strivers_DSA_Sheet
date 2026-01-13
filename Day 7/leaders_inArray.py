# def leaders_inArray(arr):
#     res=[]
#     for i in range(len(arr)):
#         max_ele = -1
#         for j in range(i+1,len(arr)):
#             if arr[i]<arr[j]:
#                 max_ele = -1
#                 break
#             else:
#                 max_ele = arr[i]
                
#         if max_ele != -1:
#             res.append(max_ele)
#     res.append(arr[-1])
#     return res

def leaders_inArray(arr):
    ans = []

    maxi = float('-inf')

    for i in range(len(arr)-1,-1,-1):
        if arr[i] > maxi:
            ans.append(arr[i])
            maxi = max(maxi,arr[i])

    ans.reverse()
    return ans

arr = [10, 22, 12, 3, 0, 6] 
print(leaders_inArray(arr))
# def majority_element(arr):
#     freq = {}
#     res = []
#     mini = len(arr)//3+1
#     for i in range(len(arr)):
#         freq[arr[i]] = freq.get(arr[i],0) + 1
#         if freq[arr[i]] == mini:
#             res.append(arr[i])
#         if len(res) == 2:
#             break
#     return res

def majority_element(arr):
    res = []
    n = len(arr)
    count1, count2 = 0,0
    ele1 = float('-inf')
    ele2 = float('-inf')

    for num in arr:
        if count1 == 0 and num != ele2:
            count1 = 1
            ele1 = num
        elif count2 == 0 and num != ele1:
            count2 = 1
            ele2 = num
        elif num == ele1:
            count1+=1
        elif num == ele2:
            count2+=1
        else:
            count1-=1
            count2-=1
    
    count1=0
    count2=0

    for num in arr:
        if num == ele1:
            count1+=1
        if num == ele2:
            count2+=1
    
    mini = n//3
    if count1 > mini:
        res.append(ele1)
    if count2 > mini and ele1 != ele2:
        res.append(ele2)

    return res

arr = [1, 2, 1, 1, 3, 2, 2]   
print(majority_element(arr))
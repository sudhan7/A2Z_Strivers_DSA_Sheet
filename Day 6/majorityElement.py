#Moore's voting algorithm
"""
[7,7,5,7,5,1,5,7,5,5,7,7,5,5,5,5]

take the first as an element and count as 1
el = 7
count = 1

if 7 add count+=1
if not 7 dec count-=1

if count == 0 then move to the next element and make count = 1
and repeat

at the end one element will have count > 0 it will be the majority element
"""
#step 2 verifiy

"""
verify the element found is greater than n/2 times
"""

# def majorityElement(arr):
#     freq = {}

#     for num in arr:
#         freq[num] = freq.get(num,0) + 1

#     for num, item in freq.items():
#         if item > len(arr)//2:
#             return num

def majorityElement(arr):
    el = 0
    count = 0
    for i in range(len(arr)):
        if count == 0:
            el = arr[i]
            count = 1
        elif arr[i] == el:
            count+=1
        else:
            count-=1

    count1 = 0
    for num in arr:
        if num == el:
            count1+=1
    
    if count1 > len(arr)//2:
        return el
    else:
        return -1

arr = [7,7,5,7,5,1,5,7,5,5,7,7,5,5,5,5]
print(majorityElement(arr))
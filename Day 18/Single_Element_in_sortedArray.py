# def Single_Element_in_sortedArray(arr):
#     count = {}
#     for num in arr:
#         count[num] = count.get(num,0)+1
    
#     for key, value in count.items():
#         if value == 1:
#             return key
    
#     return -1

def Single_Element_in_sortedArray(arr):
    n = len(arr)
    low = 0
    high = n-1

    if n == 1:
        return arr[0]
    if arr[0] != arr[1]:
        return arr[0]
    if arr[n-1] != arr[n-2]:
        return arr[n-1]
    
    low = 1 
    high = n-1

    while low <= high:
        mid =(low + high)//2

        if arr[mid] != arr[mid+1] and arr[mid] != arr[mid-1]:
            return arr[mid]
        
        if (mid%2)==1 and arr[mid-1] == arr[mid] or (mid%2)==0 and arr[mid+1] == arr[mid]:
            low = mid+1
        else:
            high = mid-1


arr = [1,1,2,2,3,3,4,5,5,6,6]
print(Single_Element_in_sortedArray(arr))
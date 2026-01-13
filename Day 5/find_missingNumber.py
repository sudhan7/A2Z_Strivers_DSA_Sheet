# def find_missingNumber(arr, n):
#     for i in range(1,n+1):
#         if i not in arr:
#             return i
#     return

def find_missingNumber(arr, n):
    xor1 = 0
    xor2 = 0

    for i in range(n-1):
        xor2 ^= arr[i]
        xor1 ^= (i+1)
    
    xor1 ^= n

    return xor1 ^ xor2

arr = [1,2,4,5]
N = 5
print(find_missingNumber(arr,N))
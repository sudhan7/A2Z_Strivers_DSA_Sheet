# def findNumber_appearsOnce(arr):
#     freq = {}
#     for num in arr:
#         freq[num] = freq.get(num, 0) + 1

#     for num, count in freq.items():
#         if count == 1:
#             return num

def findNumber_appearsOnce(arr):
    xor = 0
    for num in arr:
        xor ^= num
    return xor

arr = [2,2,1]
print(findNumber_appearsOnce(arr))
# def longestConsecutive_sequence(arr):
#     arr.sort()
#     longest = 1
#     lastSmall = float('-inf')
#     count = 0

#     for i in range(len(arr)):
#         if arr[i] - 1 == lastSmall:
#             count+=1
#             lastSmall = arr[i]
#         elif arr[i] - 1 != lastSmall:
#             count = 1
#             lastSmall = arr[i]
#         longest = max(longest,count)
    
#     return 

def longestConsecutive_sequence(arr):
    n = len(arr)
    longest = 1
    st = set(arr)

    for it in st:
        if it - 1 not in st:
            cnt = 1
            x = it

            while x+1 in st:
                cnt += 1
                x += 1
            
            longest = max(longest, cnt)
    
    return longest


arr = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]    
print(longestConsecutive_sequence(arr))
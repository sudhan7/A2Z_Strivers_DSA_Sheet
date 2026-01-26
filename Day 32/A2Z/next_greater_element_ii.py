def next_greater_element_ii(nums):
    stack = []
    n = len(nums)
    res = [-1] * n
    

    for i in reversed(range((2*n)-1)):
        while stack and stack[-1] <= arr[i%n]:
            stack.pop()
        if i < n:
            res[i] = -1 if not stack else stack[-1]
        stack.append(arr[i%n])
    return res

arr = [3, 10, 4, 2, 1, 2, 6, 1, 7, 2, 9]
print(next_greater_element_ii(arr))


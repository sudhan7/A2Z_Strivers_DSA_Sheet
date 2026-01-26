def next_greater_element(nums):
    stack = []
    res = [-1] * len(nums)

    for i in reversed(range(len(nums))):
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        if not stack:
            res[i] = -1
        else:
            res[i] = stack[-1]
        stack.append(nums[i])
    return res


arr = [6, 8, 0, 1, 3]
print(next_greater_element(arr))
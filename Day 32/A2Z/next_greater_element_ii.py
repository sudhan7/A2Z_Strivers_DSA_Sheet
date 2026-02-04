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


def next_greater_element_ii_forward(nums):
    n = len(nums)
    st = []
    res = [-1] * n

    for i in range(2*n):
        curr = nums[i%n]
        while st and nums[st[-1]] < curr:
            idx = st.pop()
            res[idx] = curr
        if i < n:
            st.append(i)
    return res


arr = [3, 10, 4, 2, 1, 2, 6, 1, 7, 2, 9]
print(next_greater_element_ii(arr))

arr = [3, 10, 4, 2, 1, 2, 6, 1, 7, 2, 9]
print(next_greater_element_ii_forward(arr))
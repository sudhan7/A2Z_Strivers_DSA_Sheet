def prev_greater_element(arr):
    n = len(arr)
    ans = [-1] * n
    st = []

    for i in range(n-1,-1,-1):
        while st and arr[st[-1]] <= arr[i]:
            idx = st.pop()
            ans[idx] = arr[i]
        st.append(i)
    return ans 

arr = [4, 5, 2, 10, 8]
print(prev_greater_element(arr))
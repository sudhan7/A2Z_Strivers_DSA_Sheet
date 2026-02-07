def find_temperature(arr):
    n = len(arr)
    st = []
    res = [0] * n

    for i in range(n):
        while st and arr[st[-1]] < arr[i]:
            period = i - st[-1]
            res[st[-1]] = period
            st.pop()
        st.append(i)
    return res

arr = [73,74,75,71,69,72,76,73]
print(find_temperature(arr))
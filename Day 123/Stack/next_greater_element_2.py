def NGE(arr):
    st = []
    ans = [-1] * len(arr)

    for i in range(len(arr) * 2):
        index = i % len(arr)

        while st and arr[st[-1]] < arr[index]:
            ans[st.pop()] = arr[index]
        
        if i < len(arr):
            st.append(index)
    return ans

nums = [1,2,1]
print(NGE(nums))
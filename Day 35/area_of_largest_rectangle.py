def area_of_largest_rectangle(arr):
    st = []
    max_area = 0

    for i in range(len(arr)+1):
        curr_height = arr[i] if i < n else 0
        while st and (i==n or arr[st[-1]] >= curr_height):
            height = arr[st.pop()]

            if not st:
                width = i
            else:
                width = i - st[-1] - 1
            max_area = max(max_area, height*width)
        
        st.append(i)
    return max_area


arr = [2, 1, 5, 6, 2, 3, 1]
n = len(arr)
print(area_of_largest_rectangle(arr))
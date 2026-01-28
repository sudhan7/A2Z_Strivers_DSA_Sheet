def asteroid_collision(arr):
    st = []
    for i in range(len(arr)):
        if arr[i] > 0:
            st.append(arr[i])
        else:
            while st and st[-1]>0 and st[-1] < abs(arr[i]):
                st.pop()
            if st and st[-1] == abs(arr[i]):
                st.pop()
            elif not st or st[-1] < 0:
                st.append(arr[i])
    return st

arr = [4,7,1,1,2,-3,-7,17,15,-16]
print(asteroid_collision(arr))
def pge(n,arr):
    ans = [0] * n
    st = []

    for i in range(n):
        curr_ele = arr[i]

        while st and arr[st[-1]] <= curr_ele:
            st.pop()
        
        if not st:
            ans[i] = -1
        else:
            ans[i] = st[-1]
        st.append(i)
    return ans

def Stock_span_problem(n,arr):
    PGE = pge(n,arr)
    ans = [0] * n

    for i in range(n):
        ans[i] = i - PGE[i]

    return ans

n = 7 
arr = [120, 100, 60, 80, 90, 110, 115]
print(Stock_span_problem(n,arr))
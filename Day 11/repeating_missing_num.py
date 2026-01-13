def repeating_missing_num(arr):
    ans = [-1,-1]
    n = len(arr)

    for i in range(1,n+1):
        count = arr.count(i)
        if count == 2:
            ans[0] = i
        elif count == 0:
            ans[1] = i
    return ans

arr = [1, 2, 3, 6, 7, 5, 7]
print(repeating_missing_num(arr))
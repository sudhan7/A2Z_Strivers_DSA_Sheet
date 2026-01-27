def findNSE(arr):
    res = [0] * len(arr)
    stack = []

    for i in range(len(arr)-1,-1,-1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        res[i] = stack[-1] if stack else len(arr)
        stack.append(i)
    print(res)
    return res

def findPSEE(arr):
    res = [0] * len(arr)
    stack = []

    for i in range(len(arr)):
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()
        res[i] = stack[-1] if stack else -1
        stack.append(i)
    print(res)
    return res


def sumOfSubarrayMin(arr):
    nse = findNSE(arr)
    psee = findPSEE(arr)
    mod = int(1e7+7)
    total = 0

    for i in range(len(arr)):
        left = i - psee[i]
        right = nse[i] - i
        freq = left * right * 1
        val = (freq * arr[i]) % mod
        total = (total + val) % mod
    return total

arr = [3, 1, 2, 5]
print(sumOfSubarrayMin(arr))
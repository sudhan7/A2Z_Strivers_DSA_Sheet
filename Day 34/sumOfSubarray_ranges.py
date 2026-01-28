def findNSE(arr):
    res = [0] * len(arr)
    stack = []

    for i in range(len(arr)-1,-1,-1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        res[i] = stack[-1] if stack else len(arr)
        stack.append(i)
    return res


def findPSEE(arr):
    res = [0] * len(arr)
    stack = []

    for i in range(len(arr)):
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()
        res[i] = stack[-1] if stack else -1
        stack.append(i)
    return res

def sumOfSubarray_smallest(arr):
    total = 0
    n = len(arr)

    for i in range(n):
        nse = findNSE(arr)
        psee = findPSEE(arr)
        left = i - psee[i]
        right = nse[i] - i
        freq = left * right * 1
        val = freq * arr[i]
        total += val
    return total

def findNLE(arr):
    res = [0] * len(arr)
    stack = []

    for i in range(len(arr)-1,-1,-1):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        res[i] = stack[-1] if stack else len(arr)
        stack.append(i)
    return res

def findPLEE(arr):
    res = [0] * len(arr)
    stack = []

    for i in range(len(arr)):
        while stack and arr[stack[-1]] < arr[i]:
            stack.pop()
        res[i] = stack[-1] if stack else -1
        stack.append(i)
    return res

def sumOfSubarray_largest(arr):
    total = 0
    n = len(arr)

    for i in range(n):
        nse = findNLE(arr)
        psee = findPLEE(arr)
        left = i - psee[i]
        right = nse[i] - i
        freq = left * right * 1
        val = freq * arr[i]
        total += val
    return total

def sumOfSubarray_ranges(arr):
    largest_sum = sumOfSubarray_largest(arr)
    smallest_sum = sumOfSubarray_smallest(arr)
    return largest_sum - smallest_sum

arr = [1, 3, 3]
print(sumOfSubarray_ranges(arr))
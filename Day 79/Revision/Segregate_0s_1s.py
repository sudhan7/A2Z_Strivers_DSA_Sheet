def segregate(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] == 1 and arr[right] == 0:
            arr[left], arr[right] = arr[right], arr[left]
        elif arr[left] != 1:
            left += 1
        else:
            right -= 1
    return arr

arr = [0,0,0,1,0]
print(segregate(arr))

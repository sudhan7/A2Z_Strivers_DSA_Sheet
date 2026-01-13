
def find_floor(arr, x):
    low, high = 0, len(arr) - 1
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] <= x:
            ans = arr[mid]  # Potential floor
            low = mid + 1
        else:
            high = mid - 1
    return ans

def find_ceil(arr, x):
    low, high = 0, len(arr) - 1
    ans = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= x:
            ans = arr[mid]  # Potential ceil
            high = mid - 1
        else:
            low = mid + 1
    return ans

def get_floor_and_ceil(arr, x):
    floor = find_floor(arr, x)
    ceil = find_ceil(arr, x)
    return floor, ceil

# Usage
arr = [3, 4, 4, 7, 8, 10]
x = 5
print(get_floor_and_ceil(arr, x))

def minheap_or_not(arr):
    n = len(arr)
    for i in range(n//2):
        left = 2*i+1
        if left < n and arr[i] > arr[left]:
            return False
        
        right = 2*i+2
        if right < n and arr[i] > arr[right]:
            return False
    return True

arr = [10, 20, 30, 25, 15]
print(minheap_or_not(arr))
import heapq
def kthlargest(nums,k):
    heap = []

    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap,num)
        else:
            heapq.heappushpop(heap,num)
    return heap[0]

nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(kthlargest(nums,k))

nums = [3,2,1,5,6,4]
k = 2
print(kthlargest(nums,k))

nums = [3,2,1,5,6,4]
k = 4
print(kthlargest(nums,k))
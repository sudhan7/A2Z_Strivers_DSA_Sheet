import heapq
def kth_largest(nums,k):
    heap = []
    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap,num)
        else:
            heapq.heappushpop(heap,num)
    return heap[0]

nums = [1, 2, 3, 4, 5]
k = 2
print(kth_largest(nums,k))
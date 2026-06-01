import heapq
def lastStoneWeight(stones):
    heap = [-s for s in stones]
    heapq.heapify(heap)

    while len(heap) > 1:
        y = - heapq.heappop(heap)
        x = - heapq.heappop(heap)

        if x != y:
            heapq.heappush(heap, -(y-x))
    return -heap[0] if heap else 0

arr = [2,7,4,1,8,1]
print(lastStoneWeight(arr))

arr = [1]
print(lastStoneWeight(arr))
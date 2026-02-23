import heapq
from collections import Counter,deque
def task_scheduler(arr,n):
    time = 0
    count = Counter(arr)
    max_heap = [-cnt for cnt in count.values()]
    heapq.heapify(max_heap)
    q = deque()

    while max_heap or q:
        time+=1
        if max_heap:
            cnt = 1 + heapq.heappop(max_heap)
            if cnt:
                q.append([cnt,time+n])
        
        if q and q[0][1] == time:
            heapq.heappush(max_heap, q.popleft()[0])
    return time


tasks = ["A","C","A","B","D","B"]
n = 1
print(task_scheduler(tasks,n))
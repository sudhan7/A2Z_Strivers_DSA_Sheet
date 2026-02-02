import heapq
class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

def merge_k_sortedList(arr):
    min_heap = []
    for i,node in enumerate(arr):
        if node:
            heapq.heappush(min_heap,(node.val,i,node))
    
    dummy = ListNode(0)
    tail = dummy

    while min_heap:
        val, i, node = heapq.heappop(min_heap)

        tail.next = node
        tail = tail.next

        if node.next:
            heapq.heappush(min_heap, (node.next.val, i, node.next))
    return dummy.next


list1 = ListNode(1, ListNode(4, ListNode(5)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
list3 = ListNode(2, ListNode(6))

lists = [list1, list2, list3]
result = merge_k_sortedList(lists)

# Print the merged list
while result:
    print(result.val, end="->")
    result = result.next

"""
Time Complexity:O(N * log K) ,Where N is the total number of nodes across all K linked lists. 
Each insertion and extraction operation on the min-heap takes O(log K) time, 
and we perform such operations N times (once per node). 
Hence, the overall time complexity becomes O(N * log K).

Space Complexity:O(K),The heap stores at most K nodes at any time one from each of the K linked lists. 
Therefore, the auxiliary space used by the priority queue is O(K). 
The final merged linked list uses O(1) extra space if we disregard the output list, 
as the nodes are rearranged rather than copied.

"""
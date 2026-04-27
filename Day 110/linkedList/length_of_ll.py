class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def length_of_ll(head):
    temp = head
    ans = 0
    while temp is not None:
        ans += 1 
        temp = temp.next
    return ans


ll = Node(1)
ll.next = Node(2)
ll.next.next = Node(3)
ll.next.next.next = Node(4)
ll.next.next.next.next = Node(5)
print(length_of_ll(ll))




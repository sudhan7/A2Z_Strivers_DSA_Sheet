class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next


def reverse(head):
    nextnode = None
    curr = head
    prev = None

    while curr:
        nextnode = curr.next
        curr.next = prev
        prev = curr
        curr = nextnode
    return prev

ll = Node(1)
ll.next = Node(2)
ll.next.next = Node(3)
ll.next.next.next = Node(4)
ll.next.next.next.next = Node(5)

temp = ll
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")

head = reverse(ll)

temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")
class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

# def reverse_ll(head):
#     prev = None
#     temp = head

#     while temp:
#         front = temp.next
#         temp.next = prev
#         prev = temp
#         temp = front
#     return prev

def reverse_ll(head):
    if head is None or head.next is None:
        return head
    
    newHead = reverse_ll(head.next)
    front = head.next
    front.next = head
    head.next = None

    return newHead


def printList(head):
    while head:
        print(head.data, end="->")
        head = head.next
    print()



head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
printList(head)
res = reverse_ll(head)
printList(res)
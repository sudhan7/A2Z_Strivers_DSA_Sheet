class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

def add(l1,l2):
    dummy = Node(0)
    curr = dummy

    carry = 0

    while l1 or l2 or carry:
        v1 = l1.data if l1 else 0
        v2 = l2.data if l2 else 0

        val = v1 + v2 + carry
        carry = val // 10
        val = val % 10
        curr.next = Node(val)

        curr = curr.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next



l1 = Node(2)
l1.next = Node(4)
l1.next.next = Node(3)

l2 = Node(5)
l2.next = Node(6)
l2.next.next = Node(4)

head = add(l1,l2)

temp = head
while temp:
    print(temp.data, end="->")
    temp = temp.next
print("None")
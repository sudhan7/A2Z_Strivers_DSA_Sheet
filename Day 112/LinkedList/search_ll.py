class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def search(head,key):
    temp = head
    while temp is not None:
        if temp.data == key:
            return True
        temp = temp.next
    return False

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

key = 8
print(search(head,key))

key = 5
print(search(head,key))

temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")
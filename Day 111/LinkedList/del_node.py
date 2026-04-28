class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def delete_node(node):
    node.data = node.next.data
    node.next = node.next.next

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

delete_node(ll.next.next)

temp = ll
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")
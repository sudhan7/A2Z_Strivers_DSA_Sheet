   
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insertAtEnd(head, x):
    new_node = Node(x)
    
    if head is None:
        return new_node
    
    temp = head
    while temp.next != None:
        temp = temp.next
    temp.next = new_node
    return head
    
ll = Node(1)          
ll.next = Node(2)     


insertAtEnd(ll, 3)  

temp = ll
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")
        
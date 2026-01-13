class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def find_element(self,head,element):
        temp = head

        while temp is not None:
            if temp.data == element:
                return True
            temp = temp.next
        
        return False

if __name__ == "__main__":
    
    head = Node(0)
    head.next = Node(1)
    head.next.next = Node(2)

    ll = LinkedList()
    res = ll.find_element(head,3)
    print(res)
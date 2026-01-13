class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def lengthOf_LL(self,head):
        count = 0
        temp = head

        while temp is not None:
            count+=1
            temp = temp.next
        return count
    
if __name__ == "__main__":
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)

    ll = LinkedList()
    res = ll.lengthOf_LL(head)
    print(res)
class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class linkeddlist:
    def insertAthead(self,data,head):
        newNode = Node(data,head)
        return newNode
    
    def delete_tail(self,head):
        if head is None or head.next is None:
            return None
        curr = head

        while curr.next.next is not None:
            curr = curr.next
        
        curr.next = None
        return head
    
    def printlist(self,head):
        temp = head
        while temp:
            print(temp.data, end = "->")
            temp = temp.next
        print()

if __name__ == "__main__":
    ll = linkeddlist()

    head = Node(2)
    head.next = Node(3)

    head = ll.insertAthead(1,head)
    ll.printlist(head)

    head = ll.delete_tail(head)
    ll.printlist(head)
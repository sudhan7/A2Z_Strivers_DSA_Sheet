class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

class LinkedList:
    def middle_element(self,head):
        temp = head
        slow = temp.next
        fast = temp.next.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        return slow

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    ll = LinkedList()
    res = ll.middle_element(head)
    print(res.data)

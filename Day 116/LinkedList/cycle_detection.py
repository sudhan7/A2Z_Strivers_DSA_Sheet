class Node:
    def __init__(self,data=0,next=None):
        self.data = data
        self.next = next

def cycle_detect(head):
    slow = fast = head

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True
    
    return False


ll = Node(3)
ll.next = Node(2)
ll.next.next = Node(0)
ll.next.next.next = Node(-4)
ll.next.next.next.next = ll.next

print(cycle_detect(ll))
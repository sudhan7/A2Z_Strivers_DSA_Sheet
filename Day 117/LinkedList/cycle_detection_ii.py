class Node:
    def __init__(self,data=0,next=None):
        self.data = data
        self.next = next

def cycle_detection(head):
    slow = fast = head

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            fast = head
            while fast != slow:
                fast = fast.next
                slow = slow.next
            return slow
    return None


ll = Node(3)
ll.next = Node(2)
ll.next.next = Node(0)
ll.next.next.next = Node(-4)
ll.next.next.next.next = ll.next

node = cycle_detection(ll)
print(node.data) if node else print("-1")
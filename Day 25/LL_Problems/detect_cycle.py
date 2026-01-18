class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def detect_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
         slow = slow.next
         fast = fast.next.next

         if slow == fast:
              return True
    return False

def printlist(head):
        temp = head
        while temp:
            print(temp.data, end = "->")
            temp = temp.next
        print()

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = head.next.next

    print(detect_cycle(head))

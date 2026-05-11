class Node:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next


def palindrome(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    prev = None
    while slow:
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp
    
    left,right = head, prev

    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True


ll = Node(1)
ll.next = Node(2)
ll.next.next = Node(2)
ll.next.next.next = Node(1)

print(palindrome(ll))
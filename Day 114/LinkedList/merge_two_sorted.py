class ListNode:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

def merge(l1,l2):
    dummy = ListNode(0)
    curr = dummy

    while l1 and l2:
        if l1.data < l2.data:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    
    if l1:
        curr.next = l1
    elif l2:
        curr.next = l2
    
    return dummy.next

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

head = merge(l1,l2)

temp = head
while temp:
    print(temp.data, end = "->")
    temp = temp.next
print("None")
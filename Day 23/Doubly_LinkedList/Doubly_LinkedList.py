class Node:
    def __init__(self,data,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class doubly_LL:
    def convertArr2DLL(self,arr):
        head = Node(arr[0])
        prev = head

        for i in range(1,len(arr)):
            temp = Node(arr[i],None,prev)
            prev.next = temp
            prev = temp
        return head
    
    def delete_start(self,head):
        if head == None or head.next == None:
            return None
        
        prev = head
        head = head.next
        head.prev = None
        prev.next = None

        return head
    
    def insertAttail(self,head,k):
        newNode = Node(k)

        if not head:
            return newNode
        
        tail = head
        
        while tail.next:
            tail = tail.next
        
        tail.next = newNode
        newNode.prev = tail
        return head
    
    def delete_tail(self,head):
        if not head or not head.next:
            return None
        
        tail = head

        while tail.next:
            tail = tail.next
        
        tail.prev.next = None

        return head
    
    def reverse_dll(self,head):
        temp = None
        current = head

        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp

            current = current.prev
        
        if temp is not None:
            head = temp.prev

        return head
    
    def print_DLL(self,head):
        while head:
            print(head.data, end = "->")
            head = head.next
        print()

if __name__ == "__main__":
    arr = [12, 5, 8, 7, 4]
    dll = doubly_LL()
    res = dll.convertArr2DLL(arr)
    dll.print_DLL(res)

    delete = dll.delete_start(res)
    dll.print_DLL(delete)

    add = dll.insertAttail(delete,9)
    dll.print_DLL(add)

    delete_tail = dll.delete_tail(add)
    dll.print_DLL(delete_tail)

    reverse = dll.reverse_dll(delete_tail)
    dll.print_DLL(reverse)
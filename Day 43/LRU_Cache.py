class LRUCache:
    class Node:
        def __init__(self,key,val):
            self.key = key
            self.val = val
            self.next = None
            self.prev = None

    def __init__(self, capacity:int):
        self.head = self.Node(-1,-1)
        self.tail = self.Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head

        self.capacity = capacity
        self.m = {}
    
    def addNode(self,newNode):
        temp = self.head.next
        newNode.next = temp
        newNode.prev = self.head
        self.head.next = newNode
        temp.prev = newNode
    
    def deleteNode(self,delNode):
        delprev = delNode.prev
        delnext = delNode.next
        delprev.next = delnext
        delnext.prev = delprev
    
    def get(self,key):
        if key in self.m:
            resNode = self.m[key]
            value = resNode.val
            del self.m[key]
            self.deleteNode(resNode)
            self.addNode(resNode)
            self.m[key] = self.head.next
            return value
        return -1
    
    def put(self,key,val):
        if key in self.m:
            existingNode = self.m[key]
            del self.m[key]
            self.deleteNode(existingNode)
        
        if len(self.m) == self.capacity:
            del self.m[self.tail.prev.key]
            self.deleteNode(self.tail.prev)
        
        self.addNode(self.Node(key,val))
        self.m[key] = self.head.next



if __name__ == "__main__":
    # Create cache with capacity 2
    cache = LRUCache(2)

    # Put values in cache
    cache.put(1, 1)
    cache.put(2, 2)

    # Get value for key 1
    print(cache.get(1))

    # Insert another key (evicts key 2)
    cache.put(3, 3)

    # Key 2 should be evicted
    print(cache.get(2))

    # Insert another key (evicts key 1)
    cache.put(4, 4)

    # Key 1 should be evicted
    print(cache.get(1))

    # Key 3 should be present
    print(cache.get(3))

    # Key 4 should be present
    print(cache.get(4))
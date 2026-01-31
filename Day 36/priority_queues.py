class BinaryHeap:
    def __init__(self,capacity):
        self.capacity = capacity
        self.size = 0
        self.arr = [0] * capacity
    
    def parent(self,i):
        return i//2
    
    def left(self,i):
        return 2*i+1
    
    def right(self,i):
        return 2*i+2
    
    def insert(self,x):
        if self.size == self.capacity:
            print("Heap overflow")
        
        self.arr[self.size] = x
        k = self.size
        self.size+=1

        while k != 0 and self.arr[self.parent(k)] > self.arr[k]:
            self.arr[self.parent(k)], self.arr[k] = self.arr[k], self.arr[self.parent(k)]
            k = self.parent(k)
    
    def heapify(self,ind):
        li = self.left(ind)
        ri = self.right(ind)

        smallest = ind

        if li < self.size and self.arr[li] < self.arr[smallest]:
            smallest = li
        
        if ri < self.size and self.arr[ri] < self.arr[smallest]:
            smallest = ri
        
        if smallest != ind:
            self.arr[ind], self.arr[smallest] = self.arr[smallest], self.arr[ind]
            self.heapify(smallest)

    def get_min(self):
        if self.size == 0:
            return float('inf')
        return self.arr[0]
    
    def extract_min(self):
        if self.size <= 0 :
            return float('inf')
        if self.size == 1:
            self.size -= 1
            return self.arr[0]
        
        mini = self.arr[0]
        self.arr[0] = self.arr[self.size-1]
        self.size -= 1

        self.heapify(0)
        return mini
    def decrease_key(self, i, val):
        self.arr[i] = val 
        while i != 0 and self.arr[self.parent(i)] > self.arr[i]:
            self.arr[self.parent(i)], self.arr[i] = self.arr[i], self.arr[self.parent(i)]
            i = self.parent(i)

    def delete(self, i):
        # First decrease its value to -infinity
        self.decrease_key(i, float("-inf"))
        # Then extract minimum (which removes it)
        self.extract_min()

    def print_heap(self):
        for i in range(self.size):
            print(self.arr[i], end=" ")
        print()

if __name__== "__main__":
    h = BinaryHeap(20)
    h.insert(4)
    h.insert(1)
    h.insert(2)
    h.insert(6)
    h.insert(7)
    h.insert(3)
    h.insert(8)
    h.insert(5)

    h.print_heap()
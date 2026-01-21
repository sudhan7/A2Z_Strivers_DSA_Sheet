class MinStack:
    def __init__(self):
        self.st = []
        self.mini = None
    
    def push(self, value):
        if not self.st:
            self.mini = value
            self.st.append(value)
            return
        
        if value > self.mini:
            self.st.append(value)
        else:
            self.st.append(2*value - self.mini)
            self.mini = value

    def pop(self):
        if not self.st:
            return
        
        x = self.st.pop()

        if x < self.mini:
            self.mini = 2*self.mini - x
    
    def top(self):
        if not self.st:
            return -1
        
        x = self.st[-1]

        if self.mini < x:
            return x
        
        return self.mini
    
    def getMin(self):
        return self.mini

if __name__ == "__main__":
    s = MinStack()

    # Function calls
    s.push(-2)
    s.push(0)
    s.push(-3)
    print(s.getMin(), end=" ")
    s.pop()
    print(s.top(), end=" ")
    s.pop()
    print(s.getMin())
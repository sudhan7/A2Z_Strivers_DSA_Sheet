class Minstack:
    def __init__(self):
        self.stack = []
    
    def push(self,val):
        curr_min = min(val, self.stack[-1][1] if self.stack else val)
        self.stack.append((val, curr_min))
    
    def pop(self):
        del self.stack[-1]
    
    def top(self):
        return self.stack[-1][0]
    
    def getmin(self):
        return self.stack[-1][1]


minStack = Minstack()
print(minStack.push(1))
print(minStack.push(2))
print(minStack.push(0))
print(minStack.getmin())
print(minStack.pop())
print(minStack.top())   
print(minStack.getmin()) 
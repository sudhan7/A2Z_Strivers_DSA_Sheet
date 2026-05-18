class minstack:
    def __init__(self):
        self.stack = []
    
    def push(self,val):
        self.stack.append(val)
    
    def pop(self):
        self.stack.pop()
    
    def top(self):
        return self.stack[-1]
    
    def getmin(self):
        return min(self.stack)


st = minstack()
print(st.push(1))
print(st.push(2))
print(st.getmin())
print(st.top())
print(st.pop())
print(st.top())
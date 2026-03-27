def generate(n):
    stack = []
    res = []

    def backtrack(closeN, openN):
        if openN == closeN == n:
            res.append(''.join(stack))
            return
        
        if openN < n:
            stack.append('(')
            backtrack(closeN, openN+1)
            stack.pop()
        
        if closeN < openN:
            stack.append(')')
            backtrack(closeN+1, openN)
            stack.pop
    backtrack(0,0)
    return res

n = 3
print(generate(n))
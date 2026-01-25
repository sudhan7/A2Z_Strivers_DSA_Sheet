def prefix_to_infix(s):
    stack = []
    for ch in reversed(s):
        if ch.isalnum():
            stack.append(ch)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            expr = '(' + op1 + ch + op2 + (')')
            stack.append(expr)
    return stack[-1]

s = "*A/+BCD"
print(prefix_to_infix(s))
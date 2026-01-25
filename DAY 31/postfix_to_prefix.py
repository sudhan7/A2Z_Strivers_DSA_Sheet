def postfix_to_prefix(s):
    stack = []
    for ch in s:
        if ch.isalnum():
            stack.append(ch)
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            expr = ch+op1+op2
            stack.append(expr)
    return stack[-1]

s = "ABC+*D/"
print(postfix_to_prefix(s))
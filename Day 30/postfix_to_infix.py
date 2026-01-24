def postfix_to_infix(s):
    stack = []
    for ch in s:
        if ch.isalnum():
            stack.append(ch)
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            new_ch = "(" + op1 + ch + op2 + ")"
            stack.append(new_ch)
    return stack[-1]


s = "ABC+*D/"
print(postfix_to_infix(s))
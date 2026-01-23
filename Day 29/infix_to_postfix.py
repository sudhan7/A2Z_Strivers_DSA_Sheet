def precedence(ch):
    if ch == "^":
        return 3
    if ch == "*" or ch =="/":
        return 2
    if ch == "+" or ch == "-":
        return 1
    return 0

def infix_to_postfix(exp):
    stack = []
    output = ""

    for ch in exp:
        if ch.isalnum():
            output += ch
        
        elif ch == "(":
            stack.append(ch)
        
        elif ch == ')':
            while stack and stack[-1] != "(":
                output += stack.pop()
            stack.pop()

        else:
            while stack and precedence(stack[-1]) >= precedence(ch):
                output += stack.pop()
            stack.append(ch)
    while stack:
        output += stack.pop()
    
    return output


exp = "A*(B+C)/D"
print(infix_to_postfix(exp))
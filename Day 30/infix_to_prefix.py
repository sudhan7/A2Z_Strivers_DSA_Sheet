def precedence(ch):
    if ch == "^":
        return 3
    
    if ch == "*" or ch == "/":
        return 2
    
    if ch == "+" or ch == "-":
        return 1
    
    return 0

def infix_to_prefix(s):
    #reverse s
    rev_s = ''.join(reversed(s))

    #swap bracket
    rev_s = ''.join('(' if c == ')' else ')' if c == '(' else c for c in rev_s)

    #postfix logic
    st = []
    out = ""
    for ch in rev_s:
        if ch.isalnum():
            out+=ch
        
        elif ch == "(":
            st.append(ch)
        
        elif ch == ")":
            while st and st[-1] != "(":
                out+=st.pop()
            st.pop()
        
        else:
            while st and precedence(st[-1]) >= precedence(ch):
                out+=st.pop()
            st.append(ch)
    while st:
        out+=st.pop()
    
    #reverse out
    res = out[::-1]
    return res



s = "A*(B+C)/D"
print(infix_to_prefix(s))
def reverse_polish(tokens):
    st = []
    op = ['+', '-', '*', '/']

    for item in tokens:
        if item == '+':
            st.append(st.pop() + st.pop())
        elif item == "-":
            a,b = st.pop(), st.pop()
            st.append(b-a)
        elif item == "*":
            st.append(st.pop() * st.pop())
        elif item == "/":
            a,b = st.pop(), st.pop()
            st.append(int(b/a))
        else:
            st.append(int(item))
    return st[0]


tokens = ["2","1","+","3","*"]
print(reverse_polish(tokens))
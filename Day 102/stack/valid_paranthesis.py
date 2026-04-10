def valid_parenthesis(s):
    keymap = {")" : "(", "]" : "[", "}" : "{"}
    st = []

    for br in s :
        if br == "(" or br == "[" or br == "{":
            st.append(br)
        else:
            if not st or keymap[br] != st[-1]:
                return False
            st.pop()
    return not st

s = "[{()}]"
print(valid_parenthesis(s))
def length_of_word(s):
    if s == "":
        return 0
    return 1 + length_of_word(s[1:])

s = "geeksforgeeks"
print(length_of_word(s))
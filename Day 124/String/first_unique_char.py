def first_unique(s):
    unique = {}

    for i, char in enumerate(s):
        if char not in unique:
            unique[char] = [1,i]
        else:
            unique[char][0] += 1
    
    for key,val in unique.items():
        if val[0] == 1:
            return val[1]
    return -1

s = "leetcode"
print(first_unique(s))
s = "loveleetcode"
print(first_unique(s))
s = "aabbce"
print(first_unique(s))
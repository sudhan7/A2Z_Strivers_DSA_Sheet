def palindrome(x):
    if x < 0:
        return False
    s = str(x)
    def helper(l,r):
        if l >= r:
            return True
        if s[l] != s[r]:
            return False
        return helper(l+1, r-1)
    return helper(0,len(s)-1)

x = 1221
print(palindrome(x))
def minWindow(s: str, t: str) -> str:
    if t == "":
        return ""
    countT, window = {}, {}

    for char in t:
        countT[char] = 1 + countT.get(char, 0)
    
    res = [-1,-1]
    reslen = float("inf")
    have = 0
    need = len(countT)
    l = 0

    for r in range(len(s)):
        c = s[r]
        window[c] = 1 + window.get(c, 0)

        if c in countT and window[c] == countT[c]:
            have += 1
        
        while have == need:
            if (r-l+1) < reslen:
                res = [l,r]
                reslen = r-l+1
            window[s[l]] -= 1
            if s[l] in countT and window[s[l]] < countT[s[l]]:
                have -= 1
            l+=1
    l, r = res
    return s[l:r+1] if reslen != float("inf") else ""

s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s,t))

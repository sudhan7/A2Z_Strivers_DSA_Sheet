def LongestSubstring(s):
    left = 0
    seen = []
    max_len = float('-inf')

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left+=1
        seen.append(s[right])
        max_len = max(max_len, right-left+1)
    return max_len

s = "aaabbbccc" 
print(LongestSubstring(s))
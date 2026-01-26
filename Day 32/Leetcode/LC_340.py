def longest_substring(s,k):
    max_len = 0
    freq = {}
    left = 0

    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right],0) + 1
        while len(freq) > k:
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                del freq[s[left]]
            left+=1
        max_len = max(max_len, right-left+1)
    return max_len

s = "eceba"
k = 2
print(longest_substring(s,k))
def decode_ways(s):
    def ways(i):
        if i == len(s):
            return 1
        if s[i] == 0:
            return 0
        
        result = ways(i+1)
        if i+1 < len(s) and int(s[i:i+2]) <= 26:
            result += ways(i+2)
        return result
    return ways(0)
 
s = "226"
print(decode_ways(s))
def word_break(s,wordlist):
    def solve(index, memo):
        if index == len(s):
            return True
        
        if index in memo:
            return memo[index]
        
        for word in wordlist:
            if s[index : index + len(word)] == word:
                if solve(index+len(word), memo):
                    memo[index] = True
                    return True
                
        memo[index] = False
        return False
    return solve(0,{})

s = "leetcode"
wordlist = ["leet","code"]
print(word_break(s,wordlist))
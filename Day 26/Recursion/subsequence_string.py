def helper(s,i,path,res):
    if i == len(s):
        if path != "":
            res.append(path)
        return
    helper(s,i+1,path+s[i],res)
    helper(s,i+1,path,res)

def subsequence_string(s):
    res = []
    helper(s,0,"",res)
    return res

s = "abc"
print(subsequence_string(s))

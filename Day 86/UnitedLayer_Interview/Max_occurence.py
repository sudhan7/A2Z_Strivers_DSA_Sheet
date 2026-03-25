import re
def max_occurence(s):
    full_text = ''.join(s)
    words = re.findall(r'\b[a-zA-Z]+\b',full_text.lower())
    hashmap = {}

    for word in words:
        hashmap[word] = hashmap.get(word, 0) + 1
    
    max_len = max(hashmap.values())

    ans = [word for word, count in hashmap.items() if count == max_len]

    return ans

s = [
    "Python is a versatile programming language.",
    "Many developers find that learning to code with this programming tool.",
    "The programming documentation makes it easy to code complex applications.",
    "Consistently learning new programming techniques is the best way to code."
]
print(max_occurence(s))
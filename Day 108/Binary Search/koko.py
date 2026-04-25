import math
def koko(piles,h):
    l,r = 1, max(piles)
    res = r

    while l <= r:
        k = (l+r)//2
        hours = 0
        for p in piles:
            hours += math.ceil(p/k)
        if hours <= h:
            res = min(k,res)
            r = k-1
        else:
            l = k+1
    return res

piles = [3,6,7,11]
h = 8
print(koko(piles,h))
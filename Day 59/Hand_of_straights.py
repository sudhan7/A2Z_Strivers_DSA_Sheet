from collections import Counter
import heapq
# def isNStraightHand(hand,groupSize):

#     if len(hand) % groupSize != 0:
#         return False
#     hand.sort()
#     count = Counter(hand)

#     for num in hand:
#         while count[num] > 0:
#             for i in range(groupSize):
#                 if count[num+i] <= 0:
#                     return False
#                 count[num+i] -= 1
#     return True

def isNStraightHand(hand,groupSize):

    if len(hand) % groupSize != 0:
        return False
    
    count = {}
    for num in hand:
        count[num] = 1 + count.get(num, 0)
    
    minH = list(count.keys())
    heapq.heapify(minH)

    while minH:
        first = minH[0]
        for i in range(first, first+groupSize):
            if i not in count:
                return False
            count[i] -= 1
            if count[i] == 0:
                if i != minH[0]:
                    return False
                heapq.heappop(minH)
    return True

    
hand = [2,1]
groupSize = 2
print(isNStraightHand(hand,groupSize))
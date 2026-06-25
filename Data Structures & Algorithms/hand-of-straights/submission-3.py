class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        count = {}
        for i in hand:
            count[i] = 1 + count.get(i, 0)
        
        minH = list(count.keys())
        heapq.heapify(minH)

        while minH:
            start = minH[0]
            for i in range(start, start+groupSize):
                if count.get(i, 0) == 0:
                    return False
                count[i] -= 1

                if count[i] == 0:
                    if minH[0] != i:
                        return False
                    heapq.heappop(minH)
        return True
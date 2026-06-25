class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        req = 0

        def calHrs(k):
            total = 0
            for pile in piles:
                total += math.ceil(pile/k)
            return total
        res = max(piles)
        while l <= r:
            m = (l+r)//2
            hrs = calHrs(m)
            if hrs <= h:
                r = m - 1
                res = min(m, res)
            else:
                l = m + 1
        
        return res
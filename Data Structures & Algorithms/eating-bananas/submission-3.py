class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = r

        while l <= r:
            m = (l+r)//2
            req_hours = 0
            for pile in piles:
                req_hours += math.ceil(pile/m)
            if req_hours <= h:
                k = min(m, k)
                r = m - 1
            else:
                l = m + 1
        
        return k
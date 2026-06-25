class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = r
        while l <= r:
            m = (l+r)//2
            
            time_req = self.calculate_time(m, piles)
            
            if time_req <= h:
                k = min(k, m)
                r = m - 1
            else:
                l = m + 1
        
        return k
            

        
    def calculate_time(self, m, piles):
        time_req = 0
        for pile in piles:
            time_req += math.ceil(pile/m)
        
        return time_req
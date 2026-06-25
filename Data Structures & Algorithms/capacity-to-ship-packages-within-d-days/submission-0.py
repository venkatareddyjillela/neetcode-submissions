class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        min_weight = sum(weights)
        def cal_days(k):
            days = 0
            curr = 0
            for w in weights:
                if curr + w > k:
                    days += 1
                    curr = w
                elif curr + w == k:
                    days += 1
                    curr = 0
                else:
                    curr += w
            
            if curr:
                days += 1
            
            return days
        
        while l <= r:
            mid = (l+r)//2
            min_days = cal_days(mid)
            if min_days <= days:
                min_weight = mid
                r = mid-1
            else:
                l = mid + 1
        
        return min_weight

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        min_weight = r

        def cal_days(m):
            curr_wt = 0
            req_days = 0
            for wt in weights:
                if curr_wt + wt > m:
                    req_days += 1
                    curr_wt = wt
                elif curr_wt + wt == m:
                    req_days += 1
                    curr_wt = 0
                else:
                    curr_wt += wt
            if curr_wt:
                req_days += 1

            return req_days

        while l <= r:
            m = (l+r)//2
            req_days = cal_days(m)
            if req_days <= days:
                min_weight = min(min_weight, m)
                r = m - 1
            else:
                l = m + 1
        
        return min_weight
            
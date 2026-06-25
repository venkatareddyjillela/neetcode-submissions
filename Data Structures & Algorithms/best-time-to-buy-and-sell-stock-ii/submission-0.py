class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        profit = 0
        prev = prices[0]
        curr = prices[1]
        i = 1
        while i < len(prices):
            curr = prices[i]
            if curr-prev > 0:
                profit += (curr-prev)
            prev = curr
            i += 1
        
        return profit



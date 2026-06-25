class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l, r = 0, 1
        n = len(prices)
        while r < n:
            curr = prices[r] - prices[l]
            if curr < 0:
                l = r
                r += 1
            else:
                r += 1
            profit = max(profit, curr)
        return profit
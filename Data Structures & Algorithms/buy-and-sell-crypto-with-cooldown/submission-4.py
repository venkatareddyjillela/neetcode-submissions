class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def dfs(i, buy):
            if i >= len(prices):
                return 0
            
            cooldown = dfs(i+1, buy)
            if buy:
                res = max(dfs(i+1, not buy) - prices[i], cooldown)
            else:
                res = max(dfs(i+2, not buy) + prices[i], cooldown)
            
            return res
        
        return dfs(0, True)

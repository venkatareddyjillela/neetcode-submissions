class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # n = len(coins)
        # dp = [[-1] * amount for _ in range(n)]
        # def dfs(i, curr):
        #     if i >= len(coins) or curr >= amount:
        #         if curr == amount:
        #             return 1
        #         return 0
        #     if dp[i][curr] != -1:
        #         return dp[i][curr]
        #     left = dfs(i, curr+coins[i])
        #     right = dfs(i+1, curr)
        #     dp[i][curr] = left + right
        #     return dp[i][curr]
        # return dfs(0, 0)
        n = len(coins)
        dp = [[0] * (amount+1) for _ in range(n+1)]
        for i in range(n):
            dp[i][0] = 1
        for c in range(n-1, -1, -1):
            coin = coins[c]
            for a in range(1, amount+1):
                dp[c][a] = dp[c+1][a]
                if a-coin >= 0:
                    dp[c][a] += dp[c][a-coin]
        
        return dp[0][amount]

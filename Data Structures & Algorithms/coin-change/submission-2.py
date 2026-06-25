class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Top Down
        # dp = {0: 0}
        # def dfs(curr):
        #     if curr in dp:
        #         return dp[curr]
        #     res = float('inf')
        #     for coin in coins:
        #         if curr-coin >= 0:
        #             res = min(res, 1+dfs(curr-coin))
        #     dp[curr] = res
        #     return res
        # res = dfs(amount)
        # return res if res != float('inf') else -1
                
        # Bottom Up
        dp = [amount+1] * (amount+1)
        dp[0] = 0

        for a in range(1, amount+1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1+dp[a-c])

        return dp[amount] if dp[amount] != amount+1 else -1

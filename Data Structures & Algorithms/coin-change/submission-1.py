class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {0: 0}
        def dfs(curr):
            if curr in dp:
                return dp[curr]
            res = float('inf')
            for coin in coins:
                if curr-coin >= 0:
                    res = min(res, 1+dfs(curr-coin))
            dp[curr] = res
            return res
        res = dfs(amount)
        return res if res != float('inf') else -1
                
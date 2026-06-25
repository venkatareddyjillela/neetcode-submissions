class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[-1] * amount for _ in range(n)]
        def dfs(i, curr):
            if i >= len(coins) or curr >= amount:
                if curr == amount:
                    return 1
                return 0
            if dp[i][curr] != -1:
                return dp[i][curr]
            left = dfs(i, curr+coins[i])
            right = dfs(i+1, curr)
            dp[i][curr] = left + right
            return dp[i][curr]
        return dfs(0, 0)
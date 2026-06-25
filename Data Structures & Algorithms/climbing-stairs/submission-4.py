class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {0:1, 1:1}
        def dfs(i):
            if i in dp:
                return dp[i]

            left = dfs(i-1)
            right = dfs(i-2)
            dp[i] = left + right

            return dp[i]
        return dfs(n)
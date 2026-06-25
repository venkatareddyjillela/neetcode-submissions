class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1] * n for _ in range(m)]
        dp[m-1][n-1] = 1
        def dfs(r, c):
            if r >= m or c >= n:
                return 0

            if dp[r][c] != -1:
                return dp[r][c]

            res = dfs(r+1, c) + dfs(r, c+1)
            dp[r][c] = res
            return res
        return dfs(0, 0)
            
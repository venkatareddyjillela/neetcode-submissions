class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[-1] * (n+1) for _ in range(m+1)]

        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                res = 500
                if dp[r+1][c] != -1:
                    res = min(res, dp[r+1][c])
                if dp[r][c+1] != -1:
                    res = min(res, dp[r][c+1])
                if dp[r+1][c] == -1 and dp[r][c+1] == -1:
                    res = 0
                dp[r][c] = grid[r][c] + res
        
        return dp[0][0]
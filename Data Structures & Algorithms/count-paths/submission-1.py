class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        directions = [[1, 0], [0, 1]]
        dp = [[-1] * n for _ in range(m)]
        dp[m-1][n-1] = 1
        def dfs(r, c):
            if dp[r][c] != -1:
                return dp[r][c]
            res = 0
            for dr, dc in directions:
                rd, cd = r + dr, c + dc
                if (rd >= m or cd >= n):
                    continue
                res += dfs(rd, cd)
            dp[r][c] = res
            return res
        return dfs(0, 0)
            
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # Top down approach (memoization)
        # m, n = len(obstacleGrid), len(obstacleGrid[0])
        # dp = [[-1] * (n) for _ in range(m)]
        # dp[m-1][n-1] = 1
        
        # def dfs(r, c):
        #     if r >= m or c >= n or obstacleGrid[r][c] == 1:
        #         return 0
        #     if dp[r][c] != -1:
        #         return dp[r][c]

        #     res = dfs(r+1, c) + dfs(r, c+1)
        #     dp[r][c] = res
        #     return res
        
        # return dfs(0, 0)

        # Bottom Up approach (DP)
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * (n+1) for _ in range(m+1)]
        if obstacleGrid[m-1][n-1] == 1:
            return 0
        dp[m-1][n-1] = 1

        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if r >= m or c >= n or obstacleGrid[r][c] == 1:
                    continue
                dp[r][c] += dp[r+1][c] + dp[r][c+1]
        return dp[0][0]
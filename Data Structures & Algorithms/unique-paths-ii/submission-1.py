class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[-1] * (n) for _ in range(m)]
        dp[m-1][n-1] = 1
        
        def dfs(r, c):
            if r >= m or c >= n or obstacleGrid[r][c] == 1:
                return 0
            # if r == m-1 and c == n-1:
            #     return 1
            if dp[r][c] != -1:
                return dp[r][c]
            res = dfs(r+1, c) + dfs(r, c+1)
            dp[r][c] = res
            return res
        
        return dfs(0, 0)
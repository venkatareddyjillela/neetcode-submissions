class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        obstacles = set()
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        for r in range(m):
            for c in range(n):
                if obstacleGrid[r][c] == 1:
                    obstacles.add((r, c))
        if (0, 0) in obstacles:
            return 0
        obstacles.add((m-1, n-1))

        dp = [[0] * (n+1) for _ in range(m+1)]

        dp[m-1][n-1] = 1

        # def dfs(r, c):
        #     if r >= m or c >= n or (r, c) in obstacles:
        #         return 0
            
        #     if dp[r][c] != -1:
        #         return dp[r][c]
            
        #     dp[r][c] = dfs(r+1, c) + dfs(r, c+1)

        #     return dp[r][c]
        
        # return dfs(0, 0)

        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1 ):
                if (r, c) in obstacles:
                    continue
                dp[r][c] = dp[r+1][c] + dp[r][c+1]
                
        return dp[0][0]

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        directions = [[1, 0], [0, 1]]
        dp = [[-1] * n for _ in range(m)]
        dp[m-1][n-1] = 1
        # def dfs(r, c):
        #     if r < 0 or r >= m or c < 0 or c >= n:
        #         return 0

        #     if dp[r][c] != -1:
        #         return dp[r][c]

        #     dp[r][c] = 0
        #     for dr, dc in directions:
        #         dp[r][c] += dfs(r+dr, c+dc)
            
        #     return dp[r][c]
        
        # return dfs(0, 0)


        for r in range(m-1, -1, -1):
            dp[r][n-1] = 1

        for c in range(n-1, -1, -1):
            dp[m-1][c] = 1

        for r in range(m-2, -1, -1):
            for c in range(n-2, -1, -1):
                dp[r][c] = dp[r+1][c] + dp[r][c+1]
        
        return dp[0][0]
        



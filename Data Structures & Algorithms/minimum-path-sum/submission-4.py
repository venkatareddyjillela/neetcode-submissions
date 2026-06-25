class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dp = [[float('inf')] * (COLS+1) for _ in range(ROWS+1)]
        dp[ROWS-1][COLS-1] = 0
        def dfs(r, c):
            
            if dp[r][c] < float('inf'):
                return dp[r][c]
            
            if r+1 < ROWS:
                dp[r][c] = min(dp[r][c], grid[r+1][c] + dfs(r+1, c))
            if c+1 < COLS:
                dp[r][c] = min(dp[r][c], grid[r][c+1] + dfs(r, c+1))
            return dp[r][c]
        
        return dfs(0, 0) + grid[0][0]
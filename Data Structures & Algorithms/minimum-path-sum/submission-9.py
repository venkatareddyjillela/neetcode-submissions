class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        # if ROWS == 1 and COLS == 1:
        #     return grid[0][0]
        # dp = [[float('inf')] * (COLS+1) for _ in range(ROWS+1)]
        # dp[ROWS-1][COLS-1] = 0
        # def dfs(r, c):
        #     if dp[r][c] < float('inf'):
        #         return dp[r][c]

        #     if r+1 < ROWS:
        #         dp[r][c] = min(dp[r][c], grid[r+1][c] + dfs(r+1, c))
        #     if c+1 < COLS:
        #         dp[r][c] = min(dp[r][c], grid[r][c+1] + dfs(r, c+1))
        #     return dp[r][c]
        
        # return dfs(0, 0) + grid[0][0]

        dp = [[-1] * (COLS+1) for _ in range(ROWS+1)]

        for r in range(ROWS-1, -1, -1):
            for c in range(COLS-1, -1, -1):
                res = float('inf')
                if dp[r+1][c] != -1:
                    res = min(res, dp[r+1][c])
                if dp[r][c+1] != -1:
                    res = min(res, dp[r][c+1])
                
                if dp[r+1][c] == -1 and dp[r][c+1] == -1:
                    res = 0
                
                dp[r][c] = grid[r][c] + res
        
        return dp[0][0]




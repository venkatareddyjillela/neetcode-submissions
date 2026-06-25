class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        R, C = len(grid), len(grid[0])
        def dfs(r, c):
            if r < 0 or r >= R or c < 0 or c >= C or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0

            return 1 + dfs(r, c+1) + dfs(r, c-1) + dfs(r+1, c) + dfs(r-1, c)
        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    res = dfs(r, c)
                    maxArea = max(res, maxArea)
        return maxArea
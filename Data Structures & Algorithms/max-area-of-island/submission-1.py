class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        visited = set()
        R = len(grid)
        C = len(grid[0])

        def dfs(r, c):
            if r >= R or c >= C or r < 0 or c < 0 or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c-1) + dfs(r, c+1)

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    print(area)
                    maxArea = max(area, maxArea)
        
        return maxArea



            

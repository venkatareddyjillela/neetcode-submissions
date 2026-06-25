class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visit = set()
        max_area = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visit or grid[r][c] == 0:
                return 0
            visit.add((r, c))
            res = 1
            for dr, dc in directions:
                res += dfs(r+dr, c+dc)
            return res
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    curr_area = dfs(r, c)
                    max_area = max(curr_area, max_area)
        
        return max_area
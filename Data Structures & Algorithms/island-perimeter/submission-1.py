class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if r < 0 or r >= R or c < 0 or c >= C or grid[r][c] == 0:
                return 1

            if (r, c) in visit:
                return 0
            
            visit.add((r, c))

            res = dfs(r, c+1) + dfs(r, c-1) + dfs(r-1, c) + dfs(r+1, c)
            return res

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    return dfs(r, c)
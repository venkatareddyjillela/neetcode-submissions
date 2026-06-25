class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visited = set()
        R = len(grid)
        C = len(grid[0])

        def dfs(r, c):
            if r >= R or c >= C or r < 0 or c < 0 or grid[r][c] == '0':
                return
            
            grid[r][c] = '0'
            
            dfs(r+1, c)
            dfs(r, c+1)
            dfs(r-1, c)
            dfs(r, c-1)
            return

        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1':
                    dfs(r, c)
                    count += 1

        return count
            
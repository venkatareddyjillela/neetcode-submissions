class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        q = deque()
        R, C = len(grid), len(grid[0])
        taken = 0

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    fresh += 1
                
                elif grid[r][c] == 2:
                    q.append((r, c))

        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        
        while fresh and q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    rdr = r+dr
                    cdc = c+dc
                    if rdr < 0 or rdr >= R or cdc < 0 or cdc >= C or grid[rdr][cdc] != 1:
                        continue
                    grid[rdr][cdc] = 2
                    fresh -= 1
                    q.append((rdr, cdc))
            taken += 1

        if fresh:
            return -1
        return taken
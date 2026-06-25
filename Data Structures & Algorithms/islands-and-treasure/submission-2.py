class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2**31 - 1
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    if r+dr < 0 or r+dr >= ROWS or c+dc < 0 or c+dc >= COLS or grid[r+dr][c+dc] != INF:
                        continue
                    grid[r+dr][c+dc] = 1 + grid[r][c]
                    q.append((r+dr, c+dc))
        
            
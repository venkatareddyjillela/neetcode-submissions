class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visit = set()
        q = deque()
        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visit.add((r, c))
                if grid[r][c] == 1:
                    fresh += 1
        time = 0
        while q and fresh:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    if r+dr < 0 or r+dr >= ROWS or c+dc < 0 or c+dc >= COLS or (r+dr, c+dc) in visit or grid[r+dr][c+dc] != 1:
                        continue
                    visit.add((r+dr, c+dc))
                    fresh -= 1
                    q.append((r+dr, c+dc))
            print(q)
            time += 1
        return time if fresh == 0 else -1
        
            
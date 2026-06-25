class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        R, C = len(grid), len(grid[0])
        INF = 2147483647

        q = deque()
        visit = set()

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))
        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        dist = 1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    if r+dr < 0 or r+dr >= R or c+dc < 0 or c+dc >= C or grid[r+dr][c+dc] != INF or (r+dr, c+dc) in visit:
                        continue
                    q.append((r+dr, c+dc))
                    grid[r+dr][c+dc] = dist
            dist += 1
    
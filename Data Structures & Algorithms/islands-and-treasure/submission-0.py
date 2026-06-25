class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2 ** 31 - 1
        R = len(grid)
        C = len(grid[0])
        q = deque()
        visited = set()

        def addRoom(r, c):
            if r >= R or c >= C or r < 0 or c < 0 or grid[r][c] == -1 or (r, c) in visited:
                return
            visited.add((r, c))
            q.append([r, c])

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visited.add((r, c))

        dist = 0

        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                grid[r][c] = dist

                addRoom(r+1, c)
                addRoom(r-1, c)
                addRoom(r, c+1)
                addRoom(r, c-1)

            dist += 1

        
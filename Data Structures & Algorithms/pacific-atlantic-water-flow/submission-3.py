class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        pacific = set()
        atlantic = set()
        res = []

        pacific_q = deque()
        atlantic_q = deque()
        for c in range(COLS):
            pacific.add((0, c))
            pacific_q.append((0, c))
            atlantic.add((ROWS-1, c))
            atlantic_q.append((ROWS-1, c))
        
        for r in range(ROWS):
            pacific.add((r, 0))
            pacific_q.append((r, 0))
            atlantic.add((r, COLS-1))
            atlantic_q.append((r, COLS-1))
        
        while pacific_q:
            r, c = pacific_q.popleft()
            for dr, dc in directions:
                if r+dr < 0 or c+dc < 0 or r+dr >= ROWS or c+dc >= COLS or (r+dr, c+dc) in pacific or heights[r][c] > heights[r+dr][c+dc]:
                    continue
                pacific.add((r+dr, c+dc))
                pacific_q.append((r+dr, c+dc))

        while atlantic_q:
            r, c = atlantic_q.popleft()
            for dr, dc in directions:
                if r+dr < 0 or c+dc < 0 or r+dr >= ROWS or c+dc >= COLS or (r+dr, c+dc) in atlantic or heights[r][c] > heights[r+dr][c+dc]:
                    continue
                atlantic.add((r+dr, c+dc))
                atlantic_q.append((r+dr, c+dc))

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])

        return res
        



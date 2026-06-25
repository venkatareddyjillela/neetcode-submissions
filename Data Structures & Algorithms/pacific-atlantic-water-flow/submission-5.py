class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        pacific = set()
        atlantic = set()
        res = []

        def dfs(r, c, visit):
            visit.add((r, c))
            for dr, dc in directions:
                if r+dr < 0 or c+dc < 0 or r+dr >= ROWS or c+dc >= COLS or (r+dr, c+dc) in visit or heights[r][c] > heights[r+dr][c+dc]:
                    continue
                dfs(r+dr, c+dc, visit)

        for c in range(COLS):
            dfs(0, c, pacific)
            dfs(ROWS-1, c, atlantic)
        
        for r in range(ROWS):
            dfs(r, 0, pacific)
            dfs(r, COLS-1, atlantic)

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])

        return res
        



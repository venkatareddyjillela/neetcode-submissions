class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pacific = set()
        atlantic = set()

        R, C = len(heights), len(heights[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c, visit):
            visit.add((r, c))
            for dr, dc in directions:
                rdr, cdc = r + dr, c + dc
                if rdr < 0 or rdr >= R or cdc < 0 or cdc >= C or (rdr, cdc) in visit:
                    continue
                if heights[r][c] <= heights[rdr][cdc]:
                    dfs(rdr, cdc, visit)

            return

        for c in range(C):
            dfs(0, c, pacific)
            dfs(R-1, c, atlantic)

        for r in range(R):
            dfs(r, 0, pacific)
            dfs(r, C-1, atlantic)

        pacific = list(pacific)
        res = []

        for r, c in pacific:
            if (r, c) in atlantic:
                res.append((r, c))

        return res
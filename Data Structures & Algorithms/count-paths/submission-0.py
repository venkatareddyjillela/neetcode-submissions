class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        directions = [[1, 0], [0, 1]]
        def dfs(r, c):
            if r == m-1 and c == n-1:
                return 1
            res = 0
            for dr, dc in directions:
                rd, cd = r + dr, c + dc
                if (rd >= m or cd >= n):
                    continue
                res += dfs(rd, cd)
            return res
        return dfs(0, 0)
            
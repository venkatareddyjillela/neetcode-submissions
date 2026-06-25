class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        directions = [[1, 0], [0, 1]]
        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n:
                return 0
            
            if r == m-1 and c == n-1:
                return 1
            print(r, c)
            res = 0
            for dr, dc in directions:
                res += dfs(r+dr, c+dc)
            
            return res
        
        return dfs(0, 0)

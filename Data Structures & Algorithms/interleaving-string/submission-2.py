class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        r = len(s3)
        dp = {}
        def dfs(i, j, k):        
            if k == r:
                return i == m and j == n
            
            if (i, j) in dp:
                return dp[(i, j)]

            res = False
            if i < m and s1[i] == s3[k]:
                res = dfs(i+1, j, k+1)

            if not res and j < n and s2[j] == s3[k]:
                res = dfs(i, j+1, k+1)

            dp[(i, j)] = res
            return res
        
        return dfs(0, 0, 0)

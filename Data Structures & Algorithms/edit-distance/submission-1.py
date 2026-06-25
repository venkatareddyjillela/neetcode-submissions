class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = {}
        def dfs(i, j):
            if i == m and j == n:
                return 0
            if i == m and j < n:
                return n-j
            if j == n and i < m:
                return m-i
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            res = float('inf')
            if word1[i] == word2[j]:
                res = min(res, dfs(i+1, j+1))
            else:
                # insert
                res = min(res, 1 + dfs(i, j+1))
                # delete
                res = min(res, 1 + dfs(i+1, j))
                # replace
                res = min(res, 1 + dfs(i+1, j+1))
            dp[(i, j)] = res

            return res
        return dfs(0, 0)
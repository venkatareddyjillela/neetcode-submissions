class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Bottom Up Approach (DP)
        m, n = len(word1), len(word2)
        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(m-1, -1, -1):
            dp[i][n] = m-i

        for j in range(n-1, -1, -1):
            dp[m][j] = n-j

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    res = float('inf')
                    # insert
                    res = min(res, 1 + dp[i][j+1])
                    # delete
                    res = min(res, 1 + dp[i+1][j])
                    # replace
                    res = min(res, 1 + dp[i+1][j+1])
                    dp[i][j] = res
        return dp[0][0]
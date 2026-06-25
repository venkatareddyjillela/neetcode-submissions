class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Top Down Approach (Memoization)
        # m, n = len(text1), len(text2)
        # dp = {}

        # def dfs(i, j):
        #     if i >= m or j >= n:
        #         return 0
        #     if (i, j) in dp:
        #         return dp[(i, j)]
        #     res = 0
        #     if text1[i] == text2[j]:
        #         res = 1 + dfs(i+1, j+1)
        #     else:
        #         res = max(dfs(i+1, j), dfs(i, j+1))
        #     dp[(i, j)] = res
        #     return res
        
        # return dfs(0, 0)

        # Bottom Up Apprach (DP)
        m, n = len(text1), len(text2)
        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if text1[i] == text2[j]:
                    # if i+1 >= m or j+1 >= n:
                    #     res = 1
                    # else:
                    res = 1 + dp[i+1][j+1]
                else:
                    res = max(dp[i+1][j], dp[i][j+1])
                dp[i][j] = res
        
        return dp[0][0]
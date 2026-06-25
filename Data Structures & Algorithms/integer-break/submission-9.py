class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {0 : 1}
        def dfs(i):
            if i in dp:
                return dp[i]
            dp[i] = 0
            for j in range(1, n):
                if i - j < 0:
                    break
                
                dp[i] = max(dp[i], j * dfs(i-j))
            
            return dp[i]
        
        return dfs(n)
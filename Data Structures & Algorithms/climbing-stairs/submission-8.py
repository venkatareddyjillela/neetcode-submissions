class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {n : 1}
        def dfs(i):
            if i in dp:
                return dp[i]
            if i > n:
                return 0
            
            dp[i] = dfs(i+1) + dfs(i+2)
            return dp[i]
        
        return dfs(0)
class Solution:
    def numSquares(self, n: int) -> int:
        # dp = {0: 0}
        # def dfs(i):
        #     if i in dp:
        #         return dp[i]

        #     dp[i] = float('inf')
        #     for j in range(1, i+1):
        #         if i - j*j < 0:
        #             break
                
        #         dp[i]  = min(dp[i] , 1 + dfs(i-j*j))
            
        #     return dp[i] 
        
        # return dfs(n)

        dp = [n+1 for _ in range(n+1)]
        dp[0] = 0

        for i in range(1, n+1):
            for j in range(1, i+1):
                if i - j*j < 0:
                    break
                dp[i] = min(dp[i], 1 + dp[i-j*j])
        
        return dp[n]


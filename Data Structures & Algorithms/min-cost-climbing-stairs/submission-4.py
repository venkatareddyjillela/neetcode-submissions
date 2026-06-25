class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp = [-1] * len(cost)
        # def dfs(i):
        #     if i >= len(cost):
        #         return 0
            
        #     if dp[i] != -1:
        #         return dp[i]
            
        #     left = dfs(i+1)
        #     right = dfs(i+2)
        #     dp[i] = cost[i] + min(left, right)
        #     return dp[i]
        # return min(dfs(0), dfs(1))
        n = len(cost)
        dp = [0] * (n+1)

        for i in range(2, n+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        
        return dp[n]
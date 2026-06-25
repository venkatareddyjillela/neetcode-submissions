class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Memoization (Top down approach)
        # dp = {}
        # def dfs(i):
        #     if i >= len(cost):
        #         return 0
            
        #     if i in dp:
        #         return dp[i]
            
        #     dp[i] = cost[i] + min(dfs(i+1), dfs(i+2))

        #     return dp[i]

        # return min(dfs(0), dfs(1))

        # Bottom Up approach (DP)
        # n = len(cost)
        # dp = [-1] * n
        # dp[-1] = cost[-1]
        # dp[-2] = cost[-2]

        # for i in range(n-3, -1, -1):
        #     dp[i] = cost[i] + min(dp[i+1], dp[i+2])
        
        # return min(dp[0], dp[1])


        # Memory optimization
        n = len(cost)
        one, two = cost[-2], cost[-1]

        for i in range(n-3, -1, -1):
            temp = cost[i] + min(one, two)
            two = one
            one = temp
        
        return min(one, two)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dfs(i):
            if i >= len(cost):
                return 0
            
            left = dfs(i+1)
            right = dfs(i+2)
            return cost[i] + min(left, right)
        return min(dfs(0), dfs(1))
            
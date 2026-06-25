class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {0: 0}
        def dfs(curr):
            if curr in dp:
                return dp[curr]

            dp[curr] = float('inf')
            for i in coins:
                if curr - i >= 0:
                    dp[curr] = min(dp[curr], 1 + dfs(curr-i))
            
            return dp[curr]
        
        output = dfs(amount)
        return output if output < float('inf') else -1
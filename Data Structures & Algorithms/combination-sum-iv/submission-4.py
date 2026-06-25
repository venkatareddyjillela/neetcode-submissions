class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {0: 1}

        def dfs(curr):
            if curr in dp:
                return dp[curr]
            dp[curr] = 0
            for n in nums:
                if curr - n >= 0:
                    dp[curr] += dfs(curr-n)
            return dp[curr]
        
        return dfs(target)
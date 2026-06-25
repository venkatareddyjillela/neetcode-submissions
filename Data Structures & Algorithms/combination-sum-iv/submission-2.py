class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        # dp = {target: 1}
        # def dfs(curr):
        #     if curr > target:
        #         return 0
        #     if curr in dp:
        #         return dp[curr]
        #     res = 0
        #     for i in range(n):
        #         res += dfs(curr + nums[i])
        #     dp[curr] = res
        #     return res
        # return dfs(0)
        dp = [0] * (target+1)
        dp[0] = 1
        for i in range(1, target+1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i-num]
            
        return dp[target]
                
                
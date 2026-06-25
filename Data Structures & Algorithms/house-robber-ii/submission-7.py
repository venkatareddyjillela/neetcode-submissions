class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        first = self.helper(nums[:-1])
        second = self.helper(nums[1:])
        return max(first, second)        

    def helper(self, nums):
        dp = {}
        def dfs(i):
            if i >= len(nums):
                return 0
            
            if i in dp:
                return dp[i]
            
            dp[i] = max(dfs(i+2) + nums[i], dfs(i+1))

            return dp[i]
            
        dfs(0)
        print(dp)
        return max(dp.values())
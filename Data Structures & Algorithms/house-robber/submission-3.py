class Solution:
    def rob(self, nums: List[int]) -> int:
        # Recursion
        # n = len(nums)
        # def dfs(i):
        #     if i >= n:
        #         return 0
            
        #     return nums[i] + max(dfs(i+2), dfs(i+3))
        # return max(dfs(0), dfs(1))

        # Top down approach
        # n = len(nums)
        # dp = [-1] * (n+1)
        # def dfs(i):
        #     if i >= n:
        #         return 0
        #     if dp[i] != -1:
        #         return dp[i]
            
        #     dp[i] = nums[i] + max(dfs(i+2), dfs(i+3))
        #     return dp[i]
        # return max(dfs(0), dfs(1))

        # Bottom up approach
        n = len(nums)
        if n <= 2:
            return max(nums)
        dp = [0] * (n+1)
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        return max(dp[n], dp[n-1])
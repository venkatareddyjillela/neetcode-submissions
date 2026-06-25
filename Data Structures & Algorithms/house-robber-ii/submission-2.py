class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))
        
    def helper(self, nums):
        n = len(nums)
        dp = {}
        
        def dfs(i):
            if i >= n:
                return 0
            
            if i in dp:
                return dp[i]
            
            dp[i] = nums[i] + max(dfs(i+2), dfs(i+3))
            return dp[i]
        
        return max(dfs(0), dfs(1))

    
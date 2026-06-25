class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2
        if target < max(nums):
            return False
        
        dp = {0: True}
        
        def dfs(i, curr):
            if curr in dp:
                return dp[curr]
            
            dp[curr] = False
            for j in range(i, len(nums)):
                if curr - nums[j] >= 0:
                    if dfs(j+1, curr - nums[j]):
                        dp[curr] = True
                        break
            
            return dp[curr]
        
        return dfs(0, target)

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        res = 0
        dp = {}
        def dfs(i, curr):
            if i >= len(nums):
                if curr == target:
                    return 1
                return 0
            
            if (i, curr) in dp:
                return dp[(i, curr)]
            
            dp[(i, curr)] = dfs(i+1, curr + nums[i]) + dfs(i+1, curr - nums[i])
            return dp[(i, curr)]
        
        return dfs(0, 0)
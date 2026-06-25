class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = {len(nums)-1: 0}
        def dfs(i):
            if i in dp:
                return dp[i]
            res = len(nums)
            end = min(i+nums[i]+1, len(nums))
            for j in range(i+1, end):
                res = min(res, 1 + dfs(j))
            dp[i] = res
            return res
        return dfs(0)
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(i, curr):
            if i == len(nums):
                if curr == target:
                    return 1
                return 0
            
            res = dfs(i+1, curr-nums[i]) + dfs(i+1, curr+nums[i])

            return res
        return dfs(0, 0)
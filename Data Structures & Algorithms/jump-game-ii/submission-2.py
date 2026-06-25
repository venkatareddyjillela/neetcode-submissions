class Solution:
    def jump(self, nums: List[int]) -> int:
        # dp = {len(nums)-1: 0}
        # def dfs(i):
        #     if i in dp:
        #         return dp[i]
        #     res = len(nums)
        #     end = min(i+nums[i]+1, len(nums))
        #     for j in range(i+1, end):
        #         res = min(res, 1 + dfs(j))
        #     dp[i] = res
        #     return res
        # return dfs(0)

        # n = len(nums)
        # dp = {n-1: 0}
        # for i in range(n-2, -1, -1):
        #     res = n
        #     end = min(i+nums[i]+1, len(nums))
        #     for j in range(i+1, end):
        #         res = min(res, 1 + dp[j])
        #     dp[i] = res
        # return dp[0]

        l, r = 0, 0
        farthest = 0
        res = 0
        while r < len(nums)-1:
            for i in range(l, r+1):
                farthest = max(farthest, i + nums[i])
            l = r+1
            r = farthest
            res += 1
        return res




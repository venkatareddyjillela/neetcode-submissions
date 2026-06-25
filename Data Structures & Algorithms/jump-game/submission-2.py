class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # n = len(nums)
        # dp = {n-1: True}
        # def dfs(i):
        #     if i in dp:
        #         return dp[i]
        #     res = False
        #     for j in range(1, nums[i]+1):
        #         if i + j < n:
        #             if dfs(i+j):
        #                 res = True
        #                 break
        #     dp[i] = res
        #     return res
        # return dfs(0)

        n = len(nums)
        dp = {n-1: True}
        for i in range(n-2, -1, -1):
            res = False
            for j in range(1, nums[i]+1):
                if i + j < n:
                    if dp[i+j]:
                        res = True
                        break
            dp[i] = res
        return dp[0]
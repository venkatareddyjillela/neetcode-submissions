class Solution:
    def integerBreak(self, n: int) -> int:
        # Recursive approach
        # def dfs(target):
        #     if target == 0:
        #         return 1
        #     res = 0
        #     for i in range(1, n):
        #         if target - i < 0:
        #             break
        #         res = max(res, i * dfs(target-i))

        #     return res
        # return dfs(n)

        # Top down approach (Memoization)
        # dp = {0: 1}
        # def dfs(target):
        #     if target in dp:
        #         return dp[target]
        #     res = 0
        #     for i in range(1, n):
        #         if target - i < 0:
        #             break
        #         res = max(res, i * dfs(target-i))
        #     dp[target] = res
        #     return res
        # return dfs(n)

        # Bottom Up approach

        dp = {0: 1}
        for i in range(1, n+1):
            dp[i] = 0
            for j in range(1, n):
                if i - j < 0:
                    break
                dp[i] = max(dp[i], j * dp[i-j])
        return dp[n]




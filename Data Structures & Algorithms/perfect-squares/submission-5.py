class Solution:
    def numSquares(self, n: int) -> int:
        # recursive approach
        # def dfs(target):
        #     if target == 0:
        #         return 0
        #     res = float('inf')
        #     for i in range(1, target+1):
        #         if target - i*i >= 0:
        #             res = min(res, 1 + dfs(target - i*i))
        #         else:
        #             break
        #     return res
        # return dfs(n)

        # memoization (Top down) approach
        # dp = {0: 0}
        # def dfs(target):
        #     if target in dp:
        #         return dp[target]

        #     res = float('inf')
        #     for i in range(1, target+1):
        #         if target - i*i >= 0:
        #             res = min(res, 1 + dfs(target - i*i))
        #         else:
        #             break
        #     dp[target] = res
        #     return res
        # return dfs(n)

        # Bottom Up approach
        dp = {0: 0}

        for i in range(1, n+1):
            dp[i] = float('inf')
            for j in range(1, i+1):
                if i - j*j >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - j*j])
                else:
                    break

        return dp[n]




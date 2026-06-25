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
        dp = {0: 1}
        def dfs(target):
            if target in dp:
                return dp[target]
            res = 0
            for i in range(1, n):
                if target - i < 0:
                    break
                res = max(res, i * dfs(target-i))
            dp[target] = res
            return res
        return dfs(n)
class Solution:
    def numSquares(self, n: int) -> int:
        dp = {0: 0}
        def dfs(target):
            if target in dp:
                return dp[target]

            res = float('inf')
            for i in range(1, target+1):
                if target - i*i >= 0:
                    res = min(res, 1 + dfs(target - i*i))
                else:
                    break
            dp[target] = res
            return res
        return dfs(n)
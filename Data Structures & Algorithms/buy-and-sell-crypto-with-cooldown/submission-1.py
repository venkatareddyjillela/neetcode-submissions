class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = {}
        def dfs(i, curr):
            if i >= n:
                return 0

            if (i, curr) in dp:
                return dp[(i, curr)]

            if curr != -1:
                dp[(i, curr)] = max((prices[i] - curr) + dfs(i+2, -1), dfs(i+1, curr))
            else:
                dp[(i, curr)] = max(dfs(i+1, prices[i]), dfs(i+1, -1))
            return dp[(i, curr)]

        return dfs(0, -1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        def dfs(i, curr):
            if i >= n:
                return 0

            if curr != -1:
                res = max((prices[i] - curr) + dfs(i+2, -1), dfs(i+1, curr))
            else:
                res = max(dfs(i+1, prices[i]), dfs(i+1, -1))

            return res

        return dfs(0, -1)



class Solution:
    def climbStairs(self, n: int) -> int:
        def dfs(i):
            if i == 0 or i == 1:
                return 1

            left = dfs(i-1)
            right = dfs(i-2)

            return left + right
        return dfs(n)
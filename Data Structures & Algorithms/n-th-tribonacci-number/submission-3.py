class Solution:
    def tribonacci(self, n: int) -> int:
        # dp = [-1] * (n+1)
        # def dfs(i):
        #     if i==0:
        #         return 0
        #     if i==1:
        #         return 1
        #     if i==2:
        #         return 1
        #     if dp[i] != -1:
        #         return dp[i]
        #     dp[i] = dfs(i-1) + dfs(i-2) + dfs(i-3)
        #     return dp[i]
        # return dfs(n)
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1

        one, two, three = 1, 1, 0

        for i in range(3, n+1):
            temp = one + two + three
            three = two
            two = one
            one = temp
        return one
class Solution:
    def numDecodings(self, s: str) -> int:
        # n = len(s)
        # dp = {n: 1}

        # def dfs(i):
        #     if i in dp:
        #         return dp[i]

        #     if s[i] == '0':
        #         return 0

        #     dp[i] = dfs(i+1)
        #     if i+1 < n and (s[i] == '1' or (s[i] == '2' and int(s[i+1]) < 7)):
        #         dp[i] += dfs(i+2)

        #     return dp[i]
        
        # return dfs(0)

        n = len(s)
        two, one = 1, 1

        for i in range(n-1, -1, -1):
            if s[i] == '0':
                temp = 0
            else:
                temp = one
            if i+1 < n and (s[i] == '1' or (s[i] == '2' and int(s[i+1]) < 7)):
                temp += two
            two = one
            one = temp
        return one
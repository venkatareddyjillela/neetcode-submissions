class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = {n: 1}

        def dfs(i):
            if i in dp:
                return dp[i]

            if s[i] == '0':
                return 0

            dp[i] = dfs(i+1)
            if i+1 < n and (s[i] == '1' or (s[i] == '2' and s[i+1] in '0123456')):
                dp[i] += dfs(i+2)

            return dp[i]
        
        return dfs(0)

        # n = len(s)
        # two, one = 0, 0

        # for i in range(n):
        #     if s[i] == '0':
        #         return 0
            
        #     temp = 1 + one
        #     if 
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = {n: 1}
        def dfs(i):
            if i in dp:
                return dp[i]
            
            if s[i] == '0':
                return 0
            dp[i] = 0
            if i+1 < n and (s[i] == '1' or (s[i] == '2' and int(s[i+1] < '7'))):
                dp[i] += dfs(i+2)
            
            dp[i] += dfs(i+1)
            return dp[i]
        
        return dfs(0)
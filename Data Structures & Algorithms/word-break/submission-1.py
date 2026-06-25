class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = {n: True}
        def dfs(i):
            if i in dp:
                return dp[i]
            res = False
            for j in range(i, n):
                if s[i: j+1] in wordDict:
                    if dfs(j+1):
                        res = True
            dp[i] = res
            return res
        return dfs(0)
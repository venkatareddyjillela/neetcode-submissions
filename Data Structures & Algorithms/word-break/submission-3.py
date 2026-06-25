class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordSet = set(wordDict)
        dp = {n: True}
        def dfs(i):
            if i in dp:
                return dp[i]
            res = False
            for j in range(i, n):
                if s[i: j+1] in wordSet:
                    if dfs(j+1):
                        res = True
                        break
            dp[i] = res
            return res
        return dfs(0)
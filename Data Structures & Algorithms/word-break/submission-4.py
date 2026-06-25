class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        # wordSet = set(wordDict)
        dp = {n: True}
        def dfs(i):
            if i in dp:
                return dp[i]
            res = False
            for word in wordDict:
                if s[i : i+len(word)] == word:
                    if dfs(i+len(word)):
                        res = True
                        break
            dp[i] = res
            return res
        return dfs(0)
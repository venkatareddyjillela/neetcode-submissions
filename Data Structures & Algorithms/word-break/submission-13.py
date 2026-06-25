class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        n = len(s)
        dp = {n: True}

        def dfs(i):
            if i in dp:
                return dp[i]

            for w in words:
                if i+len(w) <= n and s[i: i+len(w)] == w:
                    if dfs(i+len(w)):
                        dp[i] = True
                        return dp[i]
 
            dp[i] = False
            return dp[i]
        
        return dfs(0)
                
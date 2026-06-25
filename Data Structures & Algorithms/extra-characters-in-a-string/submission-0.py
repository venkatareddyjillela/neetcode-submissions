class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Solution:
    def __init__(self):
        self.root = TrieNode()
        
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        words = set(dictionary)
        dp = {len(s): 0}

        def dfs(i):
            if i in dp:
                return dp[i]
            
            res = 1 + dfs(i+1)  #skip curr char
            for j in range(len(s)):
                if s[i:j+1] in words:
                    res = min(res, dfs(j+1))
            dp[i] = res
            return res
        
        return dfs(0)
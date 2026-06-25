class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.endOfWord = True

class Solution:
    def __init__(self):
        self.root = TrieNode()
        
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dp = {len(s): 0}

        trie = Trie()
        for word in dictionary:
            trie.addWord(word)

        def dfs(i):
            if i in dp:
                return dp[i]
            
            res = 1 + dfs(i+1)  #skip curr char
            curr = trie.root
            for j in range(i, len(s)):
                if s[j] not in curr.children:
                    break
                curr = curr.children[s[j]]
                if curr.endOfWord:
                    res = min(res, dfs(j+1))
            dp[i] = res
            return res
        
        return dfs(0)
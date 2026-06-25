class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Dictionary:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                new_node = TrieNode()
                curr.children[ch] = new_node
            curr = curr.children[ch]
        curr.endOfWord = True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        Trie = Dictionary()
        for word in dictionary:
            Trie.add(word)
        dp = {len(s): 0}

        def dfs(i):
            if i in dp:
                return dp[i]
            
            res = 1 + dfs(i+1)
            curr = Trie.root
            for j in range(i, len(s)):
                if s[j] not in curr.children:
                    break
                else:
                    curr = curr.children[s[j]]
                    if curr.endOfWord:
                        res = min(res, dfs(j+1))
            dp[i] = res
            return res
        return dfs(0)
            
            

        
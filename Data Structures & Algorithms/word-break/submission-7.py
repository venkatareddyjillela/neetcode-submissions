class Trie:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Dictionary:
    def __init__(self):
        self.root = Trie()

    def addWord(self, word):
        root = self.root
        for w in word:
            if w not in root.children:
                new_node = Trie()
                root.children[w] = new_node
            root = root.children[w]
        root.endOfWord = True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return True

        dp = {}
            
        dictionary = Dictionary()
        for word in wordDict:
            dictionary.addWord(word)

        def dfs(curr):
            if curr in dp:
                return dp[curr]

            trie = dictionary.root
            for i in range(len(curr)):
                if curr[i] not in trie.children:
                    dp[curr] = False
                    return False

                trie = trie.children[curr[i]]
                if trie.endOfWord:
                    if curr[i+1:] == '' or dfs(curr[i+1:]):
                        dp[curr] = True
                        return True
            
            dp[curr] = trie.endOfWord
            return dp[curr]
        return dfs(s)

            
            

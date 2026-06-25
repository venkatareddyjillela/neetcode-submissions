        
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        def dfs(i, curr):
            if i == len(word):
                if curr.endOfWord:
                    return True
                return False
            if word[i] != '.':
                if word[i] not in curr.children:
                    return False
                curr = curr.children[word[i]]
                return dfs(i+1, curr)
            
            for j in curr.children:
                if dfs(i+1, curr.children[j]):
                    return True
            return False

        return dfs(0, curr)

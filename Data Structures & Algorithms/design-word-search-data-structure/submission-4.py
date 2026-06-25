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
                new_node = TrieNode()
                curr.children[ch] = new_node
            curr = curr.children[ch]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        def dfs(i, curr):
            if i == len(word):
                return curr.endOfWord

            ch = word[i]
            if ch != '.':
                if ch not in curr.children:
                    return False
                return dfs(i+1, curr.children[ch])
                
            else:
                for j in curr.children:
                    if dfs(i+1, curr.children[j]):
                        return True
                
            return False

        return dfs(0, curr)

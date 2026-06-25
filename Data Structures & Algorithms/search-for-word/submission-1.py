class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        R = len(board)
        C = len(board[0])

        def dfs(i, r, c):
            if i == len(word):
                return True

            if r < 0 or r >= R or c < 0 or c >= C or board[r][c] != word[i] or (r, c) in visited:
                return False

            visited.add((r, c))
            res = dfs(i+1, r-1, c) or dfs(i+1, r+1, c) or dfs(i+1, r, c-1) or dfs(i+1, r, c+1)
            visited.remove((r, c))
            return res

        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(0, row, col):
                    return True
        
        return False





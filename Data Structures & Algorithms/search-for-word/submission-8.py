class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visit = set()
        R = len(board)
        C = len(board[0])

        def dfs(i, r, c):
            if i == len(word):
                return True
            if r < 0 or r >= R or c < 0 or c >= C or (r, c) in visit or board[r][c] != word[i]:
                return False
            
            visit.add((r, c))
            
            res = dfs(i+1, r+1, c) or dfs(i+1, r, c+1) or dfs(i+1, r-1, c) or dfs(i+1, r, c-1)
            visit.remove((r, c))
            return res

        for r in range(R):
            for c in range(C):
                if dfs(0, r, c):
                    return True
        
        return False
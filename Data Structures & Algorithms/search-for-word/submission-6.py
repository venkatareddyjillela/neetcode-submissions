class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        if not board:
            return False

        visit = set()

        R, C = len(board), len(board[0])
        def dfs(i, r, c):
            if i == len(word):
                return True
                
            if r < 0 or r >= R or c < 0 or c >= C or (r,c) in visit or word[i] != board[r][c]:
                return False

            visit.add((r, c))
            res = dfs(i+1, r+1, c) or dfs(i+1, r-1, c) or dfs(i+1, r, c-1) or dfs(i+1, r, c+1)
            visit.remove((r, c))
            return res

        for r in range(R):
            for c in range(C):
                res = dfs(0, r, c)
                if res:
                    return True
        
        return False
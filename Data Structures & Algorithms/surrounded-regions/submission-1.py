class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        # visit = set()

        def dfs(r, c):

            if r < 0 or r >= R or c < 0 or c >= C or board[r][c] != 'O':
                return
            board[r][c] = "T"
            for dr, dc in directions:
                dfs(r+dr, c+dc)

        R, C = len(board), len(board[0])

        for c in range(C):
            dfs(0, c)
            dfs(R-1, c)

        for r in range(R):
            dfs(r, 0)
            dfs(r, C-1)

        for r in range(R):
            for c in range(C):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'

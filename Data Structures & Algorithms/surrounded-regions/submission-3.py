class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'T'
                    if r == 0 or r == ROWS-1:
                        q.append((r, c))
                    else:
                        if c == 0 or c == COLS-1:
                            q.append((r, c))
                            
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                board[r][c] = 'O'
                for dr, dc in directions:
                    if r+dr >= 0 and c+dc >= 0 and r+dr < ROWS and c+dc < COLS:
                        if board[r+dr][c+dc] == 'T':
                            board[r+dr][c+dc] = 'O'
                            q.append((r+dr, c+dc))
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'T':
                    board[r][c] = 'X'
        



class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {i: set() for i in range(9)}
        cols = {i: set() for i in range(9)}
        boxes = {(r, c): set() for r in range(3) for c in range(3)}

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue

                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in boxes[(r//3, c//3)]:

                    print("verified")
                    print("rows[r]:", rows[r])
                    print("cols[c]:", cols[c])
                    print("boxes[(r//3, c//3)]:", boxes[(r//3, c//3)])
                    print("board[r][c]:", board[r][c])
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[(r//3, c//3)].add(board[r][c])
        
        return True

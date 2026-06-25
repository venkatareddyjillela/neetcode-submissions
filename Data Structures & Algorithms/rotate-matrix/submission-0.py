class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        # Transpose the matrix
        for r in range(n):
            for c in range(r):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        # Reverse each row in the matrix
        for i in range(n):
            l, r = 0, n-1
            while l < r:
                matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
                l += 1
                r -= 1

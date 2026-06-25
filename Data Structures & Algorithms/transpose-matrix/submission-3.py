class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])

        if m == n:
            for r in range(m):
                for c in range(r):
                    matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
            return matrix

        new_matrix = [[0] * m for _ in range(n)]

        for r in range(m):
            for c in range(n):
                new_matrix[c][r] = matrix[r][c]

        return new_matrix
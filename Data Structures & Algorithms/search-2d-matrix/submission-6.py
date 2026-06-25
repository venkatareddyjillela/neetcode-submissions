class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        l, r = 0, ROWS-1
        row = l

        while l <= r:
            m = (l+r)//2

            if matrix[m][0] <= target <= matrix[m][COLS-1]:
                row = m
                break
            elif matrix[m][0] > target :
                r = m-1
            else:
                l = m+1
        
        l, r = 0, COLS-1

        while l <= r:
            m = (l+r)//2
            val = matrix[row][m]
            if val == target:
                return True
            elif val > target:
                r = m-1
            else:
                l = m+1
        
        return False
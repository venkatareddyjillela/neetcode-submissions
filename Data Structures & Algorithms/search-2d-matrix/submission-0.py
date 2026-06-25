class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)-1
        n = len(matrix[0])-1
        L, R = 0, m
        while L <= R:
            mid = (L+R)//2
            if matrix[mid][n] < target:
                L = mid + 1
            elif matrix[mid][0] > target:
                R = mid - 1
            else:
                break
        row = matrix[mid]
        L, R = 0, len(row)-1
        while L <= R:
            mid = (L + R)//2
            val = row[mid]
            if val == target:
                return True
            elif val < target:
                L = mid+1
            else:
                R = mid - 1
        return False
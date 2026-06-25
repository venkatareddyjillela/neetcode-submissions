class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R, C = len(matrix), len(matrix[0])

        l, r = 0, R-1

        while l < r:
            mid = (l+r) // 2
            if matrix[mid][0] <= target <= matrix[mid][C-1]:
                l = mid
                break
            elif matrix[mid][0] > target:
                r = mid
            else:
                l = mid + 1
                
        req_row = l
        l, r = 0, C-1
        while l <= r:
            mid = (l+r) // 2
            if matrix[req_row][mid] == target:
                return True
            elif matrix[req_row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False
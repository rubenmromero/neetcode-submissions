class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLUMNS = len(matrix[0])
        
        left = 0
        right = ROWS * COLUMNS - 1

        while left <= right:
            mid = left + ((right - left) // 2)
            row = mid // COLUMNS
            column = mid % COLUMNS

            if matrix[row][column] == target:
                return True

            if matrix[row][column] < target:
                left = mid + 1
            else:
                right = mid - 1
            
        return False
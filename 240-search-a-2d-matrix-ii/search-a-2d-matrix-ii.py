class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix) # row 
        m = len(matrix[0]) # column
        row = n - 1
        col = 0
        
        while (row >= 0 and col < m):
            if (matrix[row][col]) == target:
                return True

            if (matrix[row][col]) > target:
                row -= 1
            else:
                col += 1

        return False
        
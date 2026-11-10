class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        top, bot = 0, len(matrix) - 1
        row = -1

        while top <= bot:
            middle = (top + bot) // 2

            if (matrix[middle][0] <= target <= matrix[middle][-1]):
                row = middle
                break
            
            elif (matrix[middle][-1] > target):
                bot = middle - 1
            
            else:
                top = middle + 1
        
        if row == -1:
            return False

        left, right = 0, len(matrix[0]) - 1
        while left <= right:
            middle = (left + right) // 2

            if (matrix[row][middle] == target):
                return True
            
            elif (matrix[row][middle] > target):
                right = middle - 1
            
            else:
                left = middle + 1
        
        return False
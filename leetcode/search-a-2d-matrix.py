class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        bot, top = 0, len(matrix) - 1
        ROW = None

        while bot <= top:
            middle = (top + bot) // 2

            if (matrix[middle][0] <= target <= matrix[middle][-1]):
                ROW = middle
                break
            
            elif (matrix[middle][-1] < target):
                bot = middle + 1
            
            else:
                top = middle - 1
        
        if (ROW is None):
            return False

        left, right = 0, len(matrix[ROW]) - 1
        while left <= right:
            middle = (right + left) // 2

            if (matrix[ROW][middle] == target):
                return True
            
            elif (matrix[ROW][middle] > target):
                right = middle - 1
            
            else:
                left = middle + 1
        
        return False
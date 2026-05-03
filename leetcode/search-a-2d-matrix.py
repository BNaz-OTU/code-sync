class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        top = 0
        bot = ROWS - 1

        while top <= bot:
            middle = (top + bot) // 2

            if (target > matrix[middle][-1]):
                top = middle + 1
            
            elif (target < matrix[middle][0]):
                bot = middle - 1
            
            else:
                break
        
        if (top > bot):
            return False
        
        row = (top + bot) // 2

        left = 0
        right = COLS - 1

        while left <= right:
            middle = (left + right) // 2

            if (target == matrix[row][middle]):
                return True
            elif (target > matrix[row][middle]):
                left = middle + 1
            else:
                right = middle -1 
        
        return False
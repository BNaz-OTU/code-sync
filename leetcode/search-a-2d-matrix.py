class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        bot, top = 0, ROWS - 1
        # bot = ROWS - 1

        while bot <= top:
            middle = (top + bot) // 2

            if (target < matrix[middle][0]):
                top = middle - 1
            
            elif (target > matrix[middle][-1]):
                bot = middle + 1
            
            else:
                break
        
        if (bot > top):
            return False
        
        row = (top + bot) // 2

        left, right = 0, COLS - 1

        while left <= right:
            middle = (left + right) // 2

            if (matrix[row][middle] == target):
                return True
            
            elif (matrix[row][middle] > target):
                right = middle -1
            
            else:
                left = middle + 1
        
        return False
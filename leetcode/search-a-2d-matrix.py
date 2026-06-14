class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bot = len(matrix) - 1

        while top <= bot:
            middle = (top + bot) // 2

            if (matrix[middle][0] <= target and target <= matrix[middle][-1]):
                break
            
            elif (target > matrix[middle][-1]):
                top = middle + 1
            
            else:
                bot = middle - 1
        
        if (top > bot):
            return False
        
        row = (top + bot) // 2

        left = 0
        right = len(matrix[0]) - 1
        while left <= right:
            middle = (left + right) // 2

            if (matrix[row][middle] == target):
                return True
            
            if (matrix[row][middle] > target):
                right = middle - 1
            
            else:
                left = middle + 1
        
        return False
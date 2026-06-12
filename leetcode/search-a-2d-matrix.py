class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bot = len(matrix) - 1

        while top <= bot:
            middle = (top + bot) // 2

            if (matrix[middle][0] <= target and target <= matrix[middle][-1]):
                break
            elif (matrix[middle][0] > target and matrix[middle][-1] > target):
                bot = middle - 1
            
            else:
                top = middle + 1
        
        if top > bot:
            return False
        
        row = (top + bot) // 2
        left, right = 0, len(matrix[row]) - 1
        while left <= right:
            mid = (left + right) // 2

            if (matrix[row][mid] == target):
                return True
            
            elif (matrix[row][mid] > target):
                right = mid - 1
            
            else:
                left = mid + 1
        
        return False
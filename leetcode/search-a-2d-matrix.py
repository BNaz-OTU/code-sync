class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_middle = len(matrix) // 2
        top = 0
        bot = len(matrix) - 1

        while (top <= bot):
            row_middle = (top + bot) // 2
            print(matrix[row_middle], top, bot)

            if (matrix[row_middle][0] <= target and target <= matrix[row_middle][-1]):
                left = 0
                right = len(matrix[0]) - 1

                while left <= right:
                    mid = (left + right) // 2

                    if (matrix[row_middle][mid] == target):
                        return True
                    
                    elif (matrix[row_middle][mid] > target):
                        right = mid - 1
                    
                    else:
                        left = mid + 1

                return False
            
            if (matrix[row_middle][0] < target):
                top = row_middle + 1
            
            else:
                bot = row_middle - 1
        
        return False
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lenOfRow = len(matrix[0])
        
        for idx in range(len(matrix)):
            print(matrix[idx])
            left = 0
            right = lenOfRow - 1

            while left <= right:
                middle = (left + right) // 2

                if (matrix[idx][middle] == target):
                    return True
                
                elif (matrix[idx][middle] > target):
                    right = middle - 1
                
                else:
                    left = middle + 1
        
        return False
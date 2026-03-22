class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for idx in range(len(matrix)):
            left = 0
            right = len(matrix[0]) - 1

            while left <= right:
                middle = right - left

                if (matrix[idx][middle] == target):
                    return True
                
                elif (matrix[idx][middle] > target):
                    right = middle - 1
                
                else:
                    left = middle + 1
        return False
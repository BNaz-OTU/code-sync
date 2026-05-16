class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowTracker = [False] * len(matrix)
        colTracker = [False] * len(matrix[0])

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if (matrix[row][col] == 0):
                    rowTracker[row] = True
                    colTracker[col] = True
        
        # print(rowTracker)
        # print(colTracker)

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if (rowTracker[row] == True):
                    matrix[row][col] = 0
                elif (colTracker[col] == True):
                    matrix[row][col] = 0
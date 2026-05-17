class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        firstRowZero = False
        ROWS, COLS = len(matrix), len(matrix[0])

        for idx in range(ROWS):
            for jdx in range(COLS):
                if (idx == 0 and matrix[idx][jdx] == 0):
                    firstRowZero = True

                if (matrix[idx][jdx] == 0):
                    matrix[0][jdx] = 0
                    if (idx != 0):
                        matrix[idx][0] = 0
        
        for row in range(1, ROWS):
            for col in range(1, COLS):
                if (matrix[0][col] == 0 or matrix[row][0] == 0):
                    matrix[row][col] = 0
        
        if (matrix[0][0] == 0):
            for row in range(ROWS):
                matrix[row][0] = 0
        
        if firstRowZero:
            for col in range(COLS):
                matrix[0][col] = 0
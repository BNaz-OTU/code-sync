class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        ROWS, COLS = len(matrix), len(matrix[0])
        firstRowZero = False

        # Determine which rows and columns should be converted to 0:
        for r in range(ROWS):
            for c in range(COLS):
                if (matrix[r][c] == 0):
                    
                    # Flag which columns need to be a zero
                    matrix[0][c] = 0

                    # Flag which rows need to be a zero
                    if r > 0:
                        matrix[r][0] = 0
                    
                    # Flag if the first row needs to be a zero
                    else:
                        firstRowZero = True
        
        # Convert most of the squares to zero (skip first row and first column)
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        # Convert the first column to 0, if necessary
        if (matrix[0][0] == 0):
            for r in range(ROWS):
                matrix[r][0] = 0

        # Convert the first row to 0, if necessary
        if (firstRowZero):
            for c in range(COLS):
                matrix[0][c] = 0
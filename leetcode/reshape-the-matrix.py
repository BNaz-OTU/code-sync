class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        ROWS, COLS = len(mat), len(mat[0])
        m = []

        if (r * c != ROWS * COLS):
            return mat
        
        for _ in range(r):
            m.append([0] * c)

        row_count = 0
        col_count = 0
        for idx in range(ROWS):
            for jdx in range(COLS):
                if (col_count == c):
                    col_count = 0
                    row_count += 1
                
                m[row_count][col_count] = mat[idx][jdx]
                col_count += 1
                

        return m
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        ROWS, COLS = len(mat), len(mat[0])

        if (ROWS * COLS != r * c):
            return mat
        
        new_mat = []
        for _ in range(r):
            new_mat.append([0] * c)
        
        r_count = 0
        c_count = 0
        for row in range(ROWS):
            for col in range(COLS):
                if (c_count == c):
                    c_count = 0
                    r_count += 1
                
                new_mat[r_count][c_count] = mat[row][col]
                c_count += 1
        
        return new_mat
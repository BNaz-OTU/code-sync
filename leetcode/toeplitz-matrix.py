class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        hashMapSubtract = {}

        for row in range(ROWS):
            for col in range(COLS):
                if ((row - col) not in hashMapSubtract):
                    hashMapSubtract[row - col] = set()
                    hashMapSubtract[row - col].add(matrix[row][col])
                
                elif ((row - col) in hashMapSubtract and (matrix[row][col] not in hashMapSubtract[row - col])):
                    # print(hashMapSubtract[row - col], " | ", matrix[row][col])
                    return False
        
        return True
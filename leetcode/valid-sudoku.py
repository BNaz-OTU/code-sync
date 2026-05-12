class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_hash = {}
        col_hash = {}
        box_hash = {}

        for idx in range(9):
            row_hash[idx] = []
            col_hash[idx] = []
        
        for jdx in range(3):
            for wdx in range(3):
                box_hash[(jdx % 3, wdx % 3)] = []
        
        for row in range(9):
            for col in range(9):
                if (board[row][col] == "."):
                    continue

                if ((board[row][col] in row_hash[row]) or
                    (board[row][col] in col_hash[col]) or
                    (board[row][col] in box_hash[(row // 3, col // 3)])):
                    return False
                
                row_hash[row].append(board[row][col])
                col_hash[col].append(board[row][col])
                box_hash[(row // 3, col // 3)].append(board[row][col])
        
        return True
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = {}
        COLS = {}
        DIAG = {}
        for idx in range(9):
            ROWS[idx] = set()
            COLS[idx] = set()
        
        for idx in range(3):
            for jdx in range(3):
                DIAG[(idx, jdx)] = set()
        
        for idx in range(9):
            for jdx in range(9):
                if (board[idx][jdx] == "."):
                    continue
                    
                if (board[idx][jdx] in ROWS[idx] or
                    board[idx][jdx] in COLS[jdx] or
                    board[idx][jdx] in DIAG[(idx // 3, jdx // 3)]):
                    return False
                
                ROWS[idx].add(board[idx][jdx])
                COLS[jdx].add(board[idx][jdx])
                DIAG[(idx // 3, jdx // 3)].add(board[idx][jdx])
        
        return True
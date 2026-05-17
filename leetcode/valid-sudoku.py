class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize the HashMap's that will record the data of duplicates
        rowHash = {}
        colHash = {}
        boxHash = {}

        for idx in range(9):
            rowHash[idx] = []
            colHash[idx] = []
        
        for idx in range(3):
            for jdx in range(3):
                boxHash[(idx, jdx)] = []
        
        # Parse through the Suduko board looking for duplicates
        for row in range(9):
            for col in range(9):
                if (board[row][col] == "."):
                    continue
                
                elif ((board[row][col] in rowHash[row] ) or
                        (board[row][col] in colHash[col]) or
                        (board[row][col] in boxHash[(row // 3, col // 3)])):
                        return False
                
                else:
                    rowHash[row].append(board[row][col])
                    colHash[col].append(board[row][col])
                    boxHash[(row // 3, col // 3)].append(board[row][col])
        
        return True
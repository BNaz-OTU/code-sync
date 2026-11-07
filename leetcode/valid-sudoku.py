class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        row_hash = {}
        col_hash = {}
        box_hash = {}

        for num in range(9):
            row_hash[num] = set()
            col_hash[num] = set()
        
        for num in range(3):
            for num2 in range(3):
                box_hash[(num % 3, num2 % 3)] = set()
        
        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if (val == "."):
                    continue
                
                if ((val in row_hash[row]) or 
                    (val in col_hash[col]) or
                    (val in box_hash[(row // 3, col // 3)])):
                    return False
                
                row_hash[row].add(val)
                col_hash[col].add(val)
                box_hash[(row // 3, col // 3)].add(val)
                
        
        return True
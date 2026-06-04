class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        # visit = set()

        # [
        # ["A","B","C","E"],
        # ["S","F","E","S"],
        # ["A","D","E","E"]
        # ]
        # "ABCE
        # SEEEFS"

        def dfs(row, col, idx, visit):
            if ((row < 0 or row >= ROWS) or
                (col < 0 or col >= COLS) or
                ((row, col) in visit) or
                (board[row][col] != word[idx])):
                return False
            
            if (idx == len(word) - 1):
                return True
            
            visit.add((row, col))
            
            return (
                dfs(row + 1, col, idx + 1, visit.copy()) or
                dfs(row - 1, col, idx + 1, visit.copy()) or
                dfs(row, col + 1, idx + 1, visit.copy()) or
                dfs(row, col - 1, idx + 1, visit.copy())
            )
            


        for row in range(ROWS):
            for col in range(COLS):
                if (board[row][col] == word[0]):
                    # visit = set()
                    if (dfs(row, col, 0, set())):
                        return True
        
        return False
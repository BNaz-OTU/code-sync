class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visit = set()

        def dfs(row, col, idx):
            if (idx == len(word)):
                return True

            if ((row < 0 or row >= ROWS) or
                (col < 0 or col >= COLS) or
                (board[row][col] != word[idx]) or
                ((row, col) in visit)):
                return False
            
            visit.add((row, col))

            holder = (
                dfs(row + 1, col, idx + 1) or 
                dfs(row - 1, col, idx + 1) or
                dfs(row, col + 1, idx + 1) or
                dfs(row, col - 1, idx + 1)
            )
            visit.remove((row, col))
            return holder

        for row in range(ROWS):
            for col in range(COLS):
                if (board[row][col] == word[0]):
                    if (dfs(row, col, 0)):
                        return True
        
        return False
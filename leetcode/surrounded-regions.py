class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        visit = set()

        def dfs(row, col):
            if ((row < 0 or row >= ROWS) or
                (col < 0 or col >= COLS) or
                (board[row][col] == "X") or
                ((row, col) in visit)):
                return
            
            board[row][col] = "T"
            visit.add((row, col))

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)


        for row in range(ROWS):
            dfs(row, 0)
            dfs(row, COLS - 1)
        
        for col in range(COLS):
            dfs(0, col)
            dfs(ROWS - 1, col)
        
        for row in range(ROWS):
            for col in range(COLS):
                if (board[row][col] == "O"):
                    board[row][col] = "X"
                
                if (board[row][col] == "T"):
                    board[row][col] = "O"
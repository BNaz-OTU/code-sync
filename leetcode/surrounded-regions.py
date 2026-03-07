class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        outsideO = []
        visit = set()

        def dfs(row, col, visit):
            if ((row < 0 or row >= ROWS) or
                (col < 0 or col >= COLS) or
                (board[row][col] == "X") or
                ((row, col) in visit)):
                return
            
            board[row][col] = "T"
            visit.add((row, col))

            dfs(row + 1, col, visit)
            dfs(row - 1, col, visit)
            dfs(row, col + 1, visit)
            dfs(row, col - 1, visit)


        for idx in range(ROWS):
            for jdx in range(COLS):
                if (idx == 0 or idx == ROWS - 1 or jdx == 0 or jdx == COLS - 1) and (board[idx][jdx] == "O"):
                    dfs(idx, jdx, visit)
        
        for idx in range(ROWS):
            for jdx in range(COLS):
                if (board[idx][jdx] == "O"):
                    board[idx][jdx] = "X"
                elif (board[idx][jdx] == "T"):
                    board[idx][jdx] = "O"
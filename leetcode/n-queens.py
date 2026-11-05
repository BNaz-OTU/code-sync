class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        final = []

        board = []
        for _ in range(n):
            board.append(["."] * n)

        colSet = set()
        posSet = set()
        negSet = set()
        def dfs(row):
            if (row == n):
                copy = board.copy()
                temp = []
                for row in copy:
                    final_row = "".join(row)
                    temp.append(final_row)
                
                final.append(temp)
                return 

            for col in range(n):
                if ((col in colSet) or ((row - col) in negSet) or ((row + col) in posSet)):
                    continue
                
                colSet.add(col)
                negSet.add((row - col))
                posSet.add((row + col))

                board[row][col] = "Q"
                dfs(row + 1)
                board[row][col] = "."

                colSet.remove(col)
                negSet.remove((row - col))
                posSet.remove((row + col))
        
        dfs(0)
        return final
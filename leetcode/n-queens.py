class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        colSet = set()
        posSet = set()
        negSet = set()
        final = []

        board = [["."] * n for _ in range(n)]

        def backtrack(row):
            if (row == n):
                copy = board.copy()
                temp = []
                for rowA in copy:
                    temp.append("".join(rowA))
                final.append(temp)

            for col in range(n):
                if (col in colSet or (row + col) in posSet or (row - col) in negSet):
                    continue
                
                board[row][col] = "Q"
                colSet.add(col)
                posSet.add(row + col)
                negSet.add(row - col)

                backtrack(row + 1)

                board[row][col] = "."
                colSet.remove(col)
                posSet.remove(row + col)
                negSet.remove(row - col)

        backtrack(0)
        
        return final
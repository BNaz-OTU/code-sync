class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        final = []
        board = [["."] * n for _ in range(n)]
        colSet, posSet, negSet = set(), set(), set()

        def dfs(row):
            if row == n:
                val = []
                for board_row in board:
                    val.append("".join(board_row))

                final.append(val)
            
            for col in range(n):
                if (col in colSet or row - col in negSet or row + col in posSet):
                    continue
                
                board[row][col] = "Q"
                colSet.add(col)
                negSet.add(row - col)
                posSet.add(row + col)

                dfs(row + 1)

                board[row][col] = "."
                colSet.remove(col)
                negSet.remove(row - col)
                posSet.remove(row + col)

        dfs(0)
        return final
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        colSet = set()
        posSet = set()
        negSet = set()
        final = []
        board = [["."] * n for _ in range(n)]

        def dfs(row):
            if (row == n):
                val = ["".join(r) for r in board]
                final.append(val)
                return

            for idx in range(n):
                if (idx in colSet or (row - idx) in negSet or (row + idx) in posSet):
                    continue
                
                board[row][idx] = "Q"
                colSet.add(idx)
                posSet.add(row + idx)
                negSet.add(row - idx)

                dfs(row + 1)

                board[row][idx] = "."
                colSet.remove(idx)
                posSet.remove(row + idx)
                negSet.remove(row - idx)

        dfs(0)
        return final
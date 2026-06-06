class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = []
        final = []
        col = set()
        posDiag = set()
        negDiag = set()

        for _ in range(n):
            board.append(["."] * n)
        
        def dfs(row):
            if (row == n):
                val = ["".join(r) for r in board]
                final.append(val)
                return 

            for num in range(n):
                if (num in col or (num + row) in posDiag or (num - row) in negDiag):
                    continue
                
                board[row][num] = "Q"
                col.add(num)
                posDiag.add((num + row))
                negDiag.add((num - row))

                dfs(row + 1)

                col.remove(num)
                posDiag.remove((num + row))
                negDiag.remove((num - row))
                board[row][num] = "."
        
        dfs(0)
        return final
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        final = []
        chess = []
        col_set, pos_set, neg_set = set(), set(), set()

        for draw_row in range(n):
            chess.append(["."] * n)
        
        def dfs(row):
            if (row == n):
                temp = ["".join(chess_row) for chess_row in chess]
                final.append(temp)
                return 

            for col in range(n):
                if col in col_set or (row - col) in neg_set or (row + col) in pos_set:
                    continue
                
                col_set.add(col)
                pos_set.add(row + col)
                neg_set.add(row - col)
                chess[row][col] = "Q"
                dfs(row + 1)
                
                col_set.remove(col)
                pos_set.remove(row + col)
                neg_set.remove(row - col)
                chess[row][col] = "."

        dfs(0)
        return final
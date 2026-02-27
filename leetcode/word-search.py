class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()
        flag = False

        def dfs(row, col, visited, wordIdx):
            if (len(word) == wordIdx):
                return True
            
            if ((row >= ROWS or row < 0) or
                (col >= COLS or col < 0) or
                ((row, col) in visited) or
                (wordIdx >= len(word)) or
                (board[row][col] != word[wordIdx])):
                return False
            
            visited.add((row, col))
            wordIdx += 1

            final = (
                dfs(row + 1, col, visited, wordIdx) or
                dfs(row - 1, col, visited, wordIdx) or
                dfs(row, col + 1, visited, wordIdx) or
                dfs(row, col - 1, visited, wordIdx)
            )

            visited.remove((row, col))

            return final

        for idx in range(ROWS):
            for jdx in range(COLS):
                if (board[idx][jdx] == word[0]):
                    flag = dfs(idx, jdx, visited, 0)

                    if (flag == True):
                        return flag
        
        return flag
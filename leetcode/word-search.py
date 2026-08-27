class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visit = set()

        def dfs(row, col, wordIdx):
            if (wordIdx == len(word)):
                return True

            if ((row < 0 or row >= ROWS) or
                (col < 0 or col >= COLS) or
                (board[row][col] != word[wordIdx]) or
                ((row, col) in visit)):
                return False
            
            visit.add((row, col))

            verdict = (
                dfs(row + 1, col, wordIdx + 1) or
                dfs(row - 1, col, wordIdx + 1) or
                dfs(row, col + 1, wordIdx + 1) or
                dfs(row, col - 1, wordIdx + 1)
            )

            if verdict == False:
                visit.remove((row, col))
                return False
            
            return True
            

        for row in range(ROWS):
            for col in range(COLS):
                if (board[row][col] == word[0] and dfs(row, col, 0)):
                    return True
        
        return False
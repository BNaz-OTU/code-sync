class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visit = set()

        def dfs(wordIdx, row, col):
            if (wordIdx == len(word)):
                return True
            
            if ((row < 0 or row >= ROWS) or
                (col < 0 or col >= COLS) or
                (board[row][col] != word[wordIdx]) or 
                ((row, col) in visit)):
                return False
            
            visit.add((row, col))

            verdict = (dfs(wordIdx + 1, row + 1, col) or
            dfs(wordIdx + 1, row - 1, col) or
            dfs(wordIdx + 1, row, col + 1) or
            dfs(wordIdx + 1, row, col - 1))

            visit.remove((row, col))
            return verdict

        for row in range(ROWS):
            for col in range(COLS):
                if (board[row][col] == word[0] and dfs(0, row, col)):
                    return True
        
        return False
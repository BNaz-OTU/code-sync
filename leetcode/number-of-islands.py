class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        counter = 0

        def dfs(row, col):
            if ((row < 0 or row >= ROWS) or
                (col < 0 or col >= COLS) or
                (grid[row][col] == "0") or
                ((row, col) in visit)):
                return
            
            visit.add((row, col))

            dfs(row + 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
            dfs(row - 1, col)

        for row in range(ROWS):
            for col in range(COLS):
                if (grid[row][col] == "1" and (row, col) not in visit):
                    counter += 1
                    dfs(row, col)
        
        return counter
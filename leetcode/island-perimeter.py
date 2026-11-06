class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        perm = 0

        def dfs(row, col):
            nonlocal perm 

            if ((row, col) in visit):
                return
            
            if ((row < 0 or row >= ROWS) or
                (col < 0 or col >= COLS) or
                (grid[row][col] == 0)):
                perm += 1
                return
            
            visit.add((row, col))

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        
        for row in range(ROWS):
            for col in range(COLS):
                if (grid[row][col] == 1):
                    dfs(row, col)
                    return perm
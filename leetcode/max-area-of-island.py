class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        visit = set()
        maxArea = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(row, col):
            if ((row < 0 or row >= ROWS) or
                (col < 0 or col >= COLS) or
                (grid[row][col] == 0) or 
                ((row, col) in visit)):
                return
            
            visit.add((row, col))

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for row in range(ROWS):
            for col in range(COLS):
                if (grid[row][col] == 1 and (row, col) not in visit):
                    prev = len(visit)
                    dfs(row, col)
                    maxArea = max(maxArea, len(visit) - prev)
        
        return maxArea
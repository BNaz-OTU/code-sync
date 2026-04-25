class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxSize = 0
        ROWS, COLS = len(grid), len(grid[0])
        allVisit = set()

        def dfs(row, col):
            if ((row < 0 or row >= ROWS) or
                (col < 0 or col >= COLS) or
                (grid[row][col] == 0) or
                ((row, col) in allVisit)):
                return
            
            allVisit.add((row, col))
            tempVisit.add((row, col))

            dfs(row, col + 1)
            dfs(row, col - 1)
            dfs(row + 1, col)
            dfs(row - 1, col)

        for row in range(ROWS):
            for col in range(COLS):
                if (grid[row][col] == 1 and (row, col) not in allVisit):
                    tempVisit = set()
                    dfs(row, col)
                    maxSize = max(maxSize, len(tempVisit))
        
        return maxSize
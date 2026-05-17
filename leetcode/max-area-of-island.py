class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        allVisit = set()
        maxIsland = 0

        def dfs(row, col):
            if ((row < 0 or row >= ROWS) or
                (col < 0 or col >= COLS) or
                (grid[row][col] == 0) or
                ((row, col) in allVisit)):
                return
            
            allVisit.add((row, col))

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for row in range(ROWS):
            for col in range(COLS):
                if (grid[row][col] == 1 and (row, col) not in allVisit):
                    prevLen = len(allVisit)
                    dfs(row, col)
                    maxIsland = max(maxIsland, len(allVisit) - prevLen)
        
        return maxIsland
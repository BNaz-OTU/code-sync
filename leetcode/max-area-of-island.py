class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        allVisited = set()
        maxCount = 0

        def dfs(row, col, visited):
            if ((row < 0 or col < 0) or (row >= ROWS or col >= COLS) or (grid[row][col] == 0) or ((row, col) in visited) or ((row, col) in allVisited)):
                return 

            if grid[row][col] == 1:
                visited.add((row, col))
                allVisited.add((row, col))
            
            return dfs(row + 1, col, visited) or dfs(row - 1, col, visited) or dfs(row, col + 1, visited) or dfs(row, col - 1, visited)

        for idx in range(len(grid)):
            for jdx in range(len(grid[idx])):
                if (grid[idx][jdx] == 1 and grid[idx][jdx] not in allVisited):
                    dfs(idx, jdx, visited)
                    maxCount = max(len(visited), maxCount)
                    visited = set()

        return maxCount
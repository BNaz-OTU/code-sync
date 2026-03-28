class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        count = 0

        def dfs(row, col, visit):
            if ((row < 0 or row >= ROWS) or
                (col < 0 or col >= COLS) or
                (grid[row][col] == "0") or
                ((row, col) in visit)):
                return 

            visit.add((row, col))

            dfs(row + 1, col, visit)
            dfs(row - 1, col, visit)
            dfs(row, col + 1, visit)
            dfs(row, col - 1, visit)

        for row in range(ROWS):
            for col in range(COLS):
                if (grid[row][col] == "1" and (row, col) not in visit):
                    count += 1
                    dfs(row, col, visit)
        
        return count
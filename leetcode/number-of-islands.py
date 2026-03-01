class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        counter = 0

        def dfs(row, col, visited):
            if ((row < 0 or row >= ROWS) or
                (col < 0 or col >= COLS) or
                ((row, col) in visited) or
                (grid[row][col] == "0")):
                return 
            
            visited.add((row, col))

            dfs(row + 1, col, visited)
            dfs(row - 1, col, visited)
            dfs(row, col + 1, visited)
            dfs(row, col - 1, visited)

        for idx in range(ROWS):
            for jdx in range(COLS):
                if (grid[idx][jdx] == "1" and (idx, jdx) not in visited):
                    dfs(idx, jdx, visited)
                    counter += 1
        
        return counter
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        counter = 0
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(row, col, visited):
            if (
                (row < 0 or col < 0) or
                (row >= ROWS or col >= COLS) or
                ((row, col) in visited) or
                (grid[row][col] == "0")
                ):
                return

            if (grid[row][col] == "1"):
                visited.add((row, col))
            
            return (
                dfs(row - 1, col, visited) or
                dfs(row + 1, col, visited) or
                dfs(row, col + 1, visited) or
                dfs(row, col - 1, visited)
            )

        for idx in range(len(grid)):
            for jdx in range(len(grid[idx])):
                if (grid[idx][jdx] == "1" and (idx, jdx) not in visited):
                    counter += 1
                    dfs(idx, jdx, visited)
                    # print(visited)

        return counter
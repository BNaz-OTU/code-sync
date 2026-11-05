class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        pacSet = set()
        atlSet = set()
        ROWS, COLS = len(heights), len(heights[0])
        final = []

        def dfs(row, col, ocean, prevHeight):
            if ((row < 0 or row >= ROWS) or
                (col < 0 or col >= COLS) or
                ((row, col) in ocean) or
                (heights[row][col] < prevHeight)):
                return
            
            ocean.add((row, col))

            dfs(row + 1, col, ocean, heights[row][col])
            dfs(row - 1, col, ocean, heights[row][col])
            dfs(row, col + 1, ocean, heights[row][col])
            dfs(row, col - 1, ocean, heights[row][col])

        for row in range(ROWS):
            dfs(row, 0, pacSet, -1)
            dfs(row, COLS - 1, atlSet, -1)
            
        for col in range(COLS):
            dfs(0, col, pacSet, -1)
            dfs(ROWS - 1, col, atlSet, -1)
        
        for coords in atlSet:
            if (coords in pacSet):
                final.append(coords)
        
        return final
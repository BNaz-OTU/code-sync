class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        atl, pac = set(), set()

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
            dfs(row, 0, pac, -1)
            dfs(row, COLS - 1, atl, -1)

        for col in range(COLS):
            dfs(0, col, pac, -1)
            dfs(ROWS - 1, col, atl, -1)

        final = []
        for row in range(ROWS):
            for col in range(COLS):
                if ((row, col) in atl and (row, col) in pac):
                    final.append([row, col])
        
        return final
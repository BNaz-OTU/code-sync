class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
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
            dfs(row, 0, pacific, -1)
            dfs(row, COLS - 1, atlantic, -1)
        
        for col in range(COLS):
            dfs(0, col, pacific, -1)
            dfs(ROWS - 1, col, atlantic, -1)
        
        for val in pacific:
            if (val in atlantic):
                final.append(val)

        return final
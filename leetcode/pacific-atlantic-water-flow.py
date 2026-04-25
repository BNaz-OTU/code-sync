class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        ROWS, COLS = len(heights), len(heights[0])

        def dfs(row, col, ocean, prevHeight):
            if ((row < 0 or row >= ROWS) or
                (col < 0 or col >= COLS) or
                ((row, col) in ocean) or
                (prevHeight > heights[row][col])):
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
        
        print(pacific)
        print(atlantic)
        final = []
        for row in range(ROWS):
            for col in range(COLS):
                if ((row, col) in pacific and (row, col) in atlantic):
                    final.append([row, col])
        
        return final
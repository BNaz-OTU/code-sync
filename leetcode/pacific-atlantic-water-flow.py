class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # USED SOLN: https://www.youtube.com/watch?v=s-VkcjHqkGI
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(row, col, visit, prevHeight):
            if ((row, col) in visit or
                (row < 0 or col < 0) or 
                (row == ROWS or col == COLS) or
                (heights[row][col] < prevHeight)):
                return
            
            visit.add((row, col))

            dfs(row + 1, col, visit, heights[row][col])
            dfs(row - 1, col, visit, heights[row][col])
            dfs(row, col + 1, visit, heights[row][col])
            dfs(row, col - 1, visit, heights[row][col])

        
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
        
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])
        
        final = []

        for idx in range(ROWS):
            for jdx in range(COLS):
                if ((idx, jdx) in pac and (idx, jdx) in atl):
                    final.append((idx, jdx))
        
        return final
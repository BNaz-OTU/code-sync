from collections import deque
# USED SOLN (didn't acc use solution but needed help explaining): https://www.youtube.com/watch?v=y704fEOx0s0
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        neighbours = [[1,0], [-1, 0], [0, -1], [0, 1]]
        minTime = 0

        fresh = 0
        rotten = deque()
        visited = set()

        for idx in range(ROWS):
            for jdx in range(COLS):
                if (grid[idx][jdx] == 2):
                    rotten.append((idx, jdx, 0))
                    visited.add((idx, jdx))
                
                if (grid[idx][jdx] == 1):
                    fresh += 1
        
        while len(rotten) > 0:
            row, col, time = rotten.popleft()

            if ((min(row, col) < 0) or
                (row >= ROWS or col >= COLS) or
                (grid[row][col] == 0)):
                continue
            
            if (grid[row][col] == 1):
                fresh -= 1

            minTime = time

            for diff_row, diff_col in neighbours:
                next_row = row + diff_row
                next_col = col + diff_col

                if ((next_row, next_col) in visited):
                    continue
                
                # if (grid[next_row])
                rotten.append((next_row, next_col, time + 1))
                visited.add((next_row, next_col))


        if (fresh != 0):
            return -1

        return minTime
        print(rotten)
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        rotten = deque()
        neighbour = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for row in range(ROWS):
            for col in range(COLS):
                if (grid[row][col] == 1):
                    fresh += 1
                elif (grid[row][col] == 2):
                    rotten.append((row, col))
        
        if (fresh == 0):
            return 0
        
        time = 0
        while len(rotten) > 0:

            if (fresh == 0):
                return time

            for _ in range(len(rotten)):
                row, col = rotten.popleft()

                for dr, dc in neighbour:
                    n_row = dr + row
                    n_col = dc + col

                    if ((n_row < 0 or n_row >= ROWS) or
                        (n_col < 0 or n_col >= COLS) or
                        (grid[n_row][n_col] == 0) or
                        (grid[n_row][n_col] == 2)):
                        continue
                    
                    grid[n_row][n_col] = 2
                    rotten.append((n_row, n_col))
                    fresh -= 1
            
            time += 1
        
        if (fresh == 0):
            return time
        else:
            return -1
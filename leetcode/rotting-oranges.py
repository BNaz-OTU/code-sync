class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        rotten = deque()
        fresh = 0
        visit = set()
        neighbours = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        for row in range(ROWS):
            for col in range(COLS):
                if (grid[row][col] == 1):
                    fresh += 1
                elif (grid[row][col] == 2):
                    rotten.append((row, col, 0))
                    visit.add((row, col))
        
        if (fresh == 0):
            return 0
        
        while len(rotten) > 0:
            c_row, c_col, time = rotten.popleft()

            for dr, dc in neighbours:
                n_row = c_row + dr
                n_col = c_col + dc

                if ((n_row < 0 or n_row >= ROWS) or
                    (n_col < 0 or n_col >= COLS) or
                    ((n_row, n_col) in visit) or 
                    (grid[n_row][n_col] == 0)):
                    continue
                
                rotten.append((n_row, n_col, time + 1))
                visit.add((n_row, n_col))
                fresh -= 1

        if (fresh == 0):
            return time

        return -1
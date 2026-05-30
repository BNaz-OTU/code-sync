class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        rotten = deque()
        neighbours = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        visit = set()

        for row in range(ROWS):
            for col in range(COLS):
                if (grid[row][col] == 1):
                    fresh += 1
                
                elif (grid[row][col] == 2):
                    rotten.append((row, col))
                    visit.add((row, col))
        
        if (fresh == 0):
            return 0
        
        time = 0
        while len(rotten) > 0:
            if (fresh == 0):
                break 

            for _ in range(len(rotten)):
                row, col = rotten.popleft()

                for dr, dc in neighbours:
                    n_row = row + dr
                    n_col = col + dc

                    if ((n_row < 0 or n_row >= ROWS) or
                        (n_col < 0 or n_col >= COLS) or
                        ((n_row, n_col) in visit) or
                        (grid[n_row][n_col] == 0)):
                        continue
                    
                    visit.add((n_row, n_col))
                    rotten.append([n_row, n_col])
                    fresh -= 1

            time += 1
        
        if (fresh != 0):
            return -1
        
        return time
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        neighbours = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        rotten = deque()
        visit = set()
        orange = 0

        for idx in range(ROWS):
            for jdx in range(COLS):
                if (grid[idx][jdx] == 2):
                    rotten.append((idx, jdx, 0))

                if (grid[idx][jdx] == 1):
                    orange += 1
        
        if (orange == 0):
            return 0
        
        while len(rotten) > 0:
            currQueue = len(rotten)

            while currQueue > 0:
                row, col, time = rotten.popleft()

                for dr, dc in neighbours:
                    n_row = row + dr
                    n_col = col + dc

                    if ((n_row < 0 or n_row >= ROWS) or
                        (n_col < 0 or n_col >= COLS) or
                        (grid[n_row][n_col] == 2 or grid[n_row][n_col] == 0) or
                        ((n_row, n_col) in visit)):
                        continue
                    
                    grid[n_row][n_col] = 2
                    orange -= 1
                    visit.add((n_row, n_col))
                    rotten.append((n_row, n_col, time + 1))

                currQueue -= 1
                
        if (orange == 0):
            print("here")
            return time
        return -1

        print(orange)
        print(len(rotten))
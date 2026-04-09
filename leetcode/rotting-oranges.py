class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        rotten = deque()
        visit = set()
        fresh = 0
        neighbours = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for row in range(ROWS):
            for col in range(COLS):
                if (grid[row][col] == 1):
                    fresh += 1
                
                elif (grid[row][col] == 2):
                    rotten.append((row, col, 0))
                    visit.add((row, col))
        
        if fresh == 0:
            return 0

        while len(rotten) > 0:
            qLen = len(rotten)
            while qLen > 0:
                row, col, time = rotten.popleft()

                # if fresh == 0:
                #     return time

                for dr, dc in neighbours:
                    n_row = row + dr
                    n_col = col + dc

                    if ((n_row < 0 or n_row >= ROWS) or
                        (n_col < 0 or n_col >= COLS) or
                        (grid[n_row][n_col] == 0) or
                        ((n_row, n_col) in visit)):
                        continue
                    
                    grid[n_row][n_col] = 2
                    fresh -= 1
                    rotten.append((n_row, n_col, time + 1))
                    visit.add((n_row, n_col))
                
                qLen -= 1
        
        if (fresh != 0):
            return -1
        return time
                

        
        print(fresh)
        print(rotten)
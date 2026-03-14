class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # USED SOLN: https://leetcode.com/problems/rotting-oranges/submissions/1943436408
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        visit = set()
        fresh = 0
        neighbours = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        for idx in range(ROWS):
            for jdx in range(COLS):
                if (grid[idx][jdx] == 2):
                    queue.append([idx, jdx, 0])
                
                if (grid[idx][jdx] == 1):
                    fresh += 1
        
        if (fresh == 0):
            return 0
        
        while len(queue) > 0:
            qLen = len(queue)

            while qLen > 0:
                row, col, length = queue.popleft()

                for dr, dc in neighbours:
                    n_row = row + dr
                    n_col = col + dc

                    if ((n_row < 0 or n_row >= ROWS) or
                        (n_col < 0 or n_col >= COLS) or
                        ((n_row, n_col) in visit) or
                        (grid[n_row][n_col] == 0) or
                        (grid[n_row][n_col] == 2)):
                        continue
                    
                    grid[n_row][n_col] = 2
                    fresh -= 1
                    visit.add((n_row, n_col))
                    queue.append([n_row, n_col, length + 1])

                qLen -= 1
    
        if (fresh == 0):
            return length
        return -1
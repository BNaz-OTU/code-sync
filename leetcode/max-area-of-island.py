class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        allVisit = set()
        tempVisit = set()
        queue = deque()
        neighbours = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        maxCount = 0

        def bfs(queue):
            while len(queue) > 0:
                cur_row, cur_col = queue.popleft()

                for d_row, d_col in neighbours:
                    n_row = cur_row + d_row
                    n_col = cur_col + d_col

                    if ((n_row < 0 or n_row >= ROWS) or
                        (n_col < 0 or n_col >= COLS) or
                        (grid[n_row][n_col] == 0) or
                        ((n_row, n_col) in allVisit)):
                        continue
                    
                    allVisit.add((n_row, n_col))
                    tempVisit.add((n_row, n_col))
                    queue.append((n_row, n_col))

        for row in range(ROWS):
            for col in range(COLS):
                if (grid[row][col] == 1 and (row, col) not in allVisit):
                    tempVisit.add((row, col))
                    allVisit.add((row, col))
                    queue.append((row, col))
                    bfs(queue)
                    maxCount = max(maxCount, len(tempVisit))
                    tempVisit = set()
        
        return maxCount
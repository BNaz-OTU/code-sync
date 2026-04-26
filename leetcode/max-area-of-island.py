class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        maxCount = 0
        neighbours = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        visit = set()
        queue = deque()

        def bfs(queue):
            counter = 0
            while len(queue) > 0:
                row, col = queue.popleft()
                counter += 1

                for dr, dc in neighbours:
                    n_row = row + dr
                    n_col = col + dc

                    if ((n_row < 0 or n_row >= ROWS) or
                        (n_col < 0 or n_col >= COLS) or
                        (grid[n_row][n_col] == 0) or
                        ((n_row, n_col) in visit)):
                        continue
                    
                    visit.add((n_row, n_col))
                    queue.append((n_row, n_col))
            return counter


        for row in range(ROWS):
            for col in range(COLS):
                if (grid[row][col] == 1 and (row, col) not in visit):
                    queue.append((row, col))
                    visit.add((row, col))
                    maxCount = max(maxCount, bfs(queue))
        
        return maxCount
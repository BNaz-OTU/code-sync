class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        allVisit = set()
        queue = deque()
        neighbours = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        maxCount = 0

        def bfs(row, col, visit, allVisit, queue):

            while len(queue) > 0:
                cur_row, cur_col = queue.popleft()

                for dr, dc in neighbours:
                    n_row = cur_row + dr
                    n_col = cur_col + dc

                    if ((n_row < 0 or n_row >= ROWS) or
                        (n_col < 0 or n_col >= COLS) or
                        ((n_row, n_col) in allVisit) or
                        (grid[n_row][n_col] == 0)):
                        continue
                    
                    queue.append((n_row, n_col))
                    visit.add((n_row, n_col))
                    allVisit.add((n_row, n_col))

        for row in range(ROWS):
            for col in range(COLS):
                if (grid[row][col] == 1 and (row, col) not in allVisit):
                    queue.append((row, col))
                    visit.add((row, col))
                    allVisit.add((row, col))
                    bfs(row, col, visit, allVisit, queue)
                    maxCount = max(maxCount, len(visit))
                    visit = set()
        
        return maxCount
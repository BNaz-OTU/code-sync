class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        allVisit = set()
        queue = deque()
        maxCount = 0
        neighbours = [[1,0], [0, 1], [-1, 0], [0, -1]]

        def bfs(queue, visit, allVisit):
            # visit.add()
            while len(queue) > 0:
                row, col = queue.popleft()

                for dr, dc in neighbours:
                    n_row = row + dr
                    n_col = col + dc

                    if ((n_row < 0 or n_row >= ROWS) or
                        (n_col < 0 or n_col >= COLS) or
                        (grid[n_row][n_col] == 0) or
                        ((n_row, n_col) in allVisit)):
                        continue
                    
                    allVisit.add((n_row, n_col))
                    visit.add((n_row, n_col))
                    queue.append([n_row, n_col])

        for row in range(ROWS):
            for col in range(COLS):
                if (grid[row][col] == 1 and (row, col) not in allVisit):
                    visit = set()
                    queue.append([row, col])
                    visit.add((row, col))
                    allVisit.add((row, col))
                    bfs(queue, visit, allVisit)
                    maxCount = max(maxCount, len(visit))
        
        return maxCount
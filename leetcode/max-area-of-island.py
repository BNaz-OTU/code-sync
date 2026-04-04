class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        allVisit = set()
        queue = deque()
        neighbours = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        maxCount = 0

        def bfs(allVisit, visit, queue):
            while len(queue) > 0:
                cur_r, cur_c = queue.popleft()
                allVisit.add((cur_r, cur_c))
                visit.add((cur_r, cur_c))

                for dr, dc in neighbours:
                    n_row = cur_r + dr
                    n_col = cur_c + dc

                    if ((n_row < 0 or n_row >= ROWS) or
                        (n_col < 0 or n_col >= COLS) or
                        ((n_row, n_col) in allVisit) or
                        (grid[n_row][n_col] == 0)):
                        continue
                    
                    queue.append([n_row, n_col])
                    allVisit.add((n_row, n_col))
                    visit.add((n_row, n_col))

                allVisit.add((row, col))

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (grid[row][col] == 1 and (row, col) not in allVisit):
                    visit = set()
                    queue.append([row, col])
                    bfs(allVisit, visit, queue)
                    maxCount = max(maxCount, len(visit))
        
        return maxCount
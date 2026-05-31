class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if (grid[0][0] == 1 or grid[-1][-1] == 1):
            return -1

        SIZE = len(grid)
        visit = set()
        queue = deque()
        queue.append((0, 0, 1))
        visit.add((0, 0))
        neighbor = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]
        mindist = 10000000

        flag = False
        while len(queue) > 0:

            for _ in range(len(queue)):
                row, col, dist = queue.popleft()

                if (row == (SIZE - 1) and col == (SIZE - 1)):
                    mindist = min(mindist, dist)
                    flag = True

                for dr, dc in neighbor:
                    n_row = row + dr
                    n_col = col + dc

                    if ((n_row < 0 or n_row >= SIZE) or
                        (n_col < 0 or n_col >= SIZE) or
                        ((n_row, n_col) in visit) or
                        (grid[n_row][n_col] == 1)):
                        continue
                    
                    visit.add((n_row, n_col))
                    queue.append((n_row, n_col, dist + 1))
        
        if (flag == False):
            return -1
            
        return mindist
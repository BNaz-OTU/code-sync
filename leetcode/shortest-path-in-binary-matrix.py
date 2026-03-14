class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if (grid[0][0] == 1 or grid[-1][-1] == 1):
            return -1
        
        SIZE = len(grid)
        visit = set()
        queue = deque()
        queue.append([0, 0, 1])
        neighbours = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]

        while len(queue) > 0:
            qlen = len(queue)
            while qlen > 0:
                row, col, length = queue.popleft()
                if (row == SIZE - 1 and col == SIZE - 1):
                    return length

                for dr, dc in neighbours:
                    n_row = row + dr
                    n_col = col + dc

                    if ((n_row < 0 or n_row >= SIZE) or 
                        (n_col < 0 or n_col >= SIZE) or 
                        (grid[n_row][n_col] == 1) or 
                        ((n_row, n_col) in visit)):
                        continue
                    
                    queue.append([n_row, n_col, length + 1])
                    visit.add((n_row, n_col))

                qlen -= 1
        
        return -1
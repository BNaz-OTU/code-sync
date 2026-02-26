class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # USED SOLN: https://www.youtube.com/watch?v=YnxUdAO7TAo

        N = len(grid)
        queue = deque([(0, 0, 1)]) # row, column, length
        visit = set((0,0))
        neighbours = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]

        while queue:
            row, col, length = queue.popleft()

            if ((min(row, col) < 0) or
                (max(row, col) >= N) or
                grid[row][col]):
                continue
            
            if (row == N - 1 and col == N - 1):
                return length
            

            for dr, dc in neighbours:
                diff_row = row + dr
                diff_col = col + dc

                if ((diff_row, diff_col) not in visit):
                    queue.append((diff_row, diff_col, length + 1))
                    visit.add((diff_row, diff_col))
        
        return -1
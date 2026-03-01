class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # USED SOLN: https://www.youtube.com/watch?v=YnxUdAO7TAo

        N = len(grid)
        queue = deque([(0, 0, 1)]) # row, column, length
        visit = set((0,0))
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]

        while len(queue) > 0:
            row, column, length = queue.popleft()
            if (min(row, column) < 0 or max(row, column) >= N or grid[row][column] == 1):
                continue
            
            if (row == N - 1 and column == N - 1):
                return length
            
            for dr, dc in directions:
                if ((row + dr, column + dc) not in visit):
                    visit.add((row + dr, column + dc))
                    queue.append((row + dr, column + dc, length + 1))
        
        return -1
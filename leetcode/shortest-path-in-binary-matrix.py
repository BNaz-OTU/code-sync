class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if (grid[0][0] == 1 or grid[-1][-1]):
            return -1
        
        neighbours = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, 1], [-1, -1], [1, -1]]
        visit = set()
        heap = [(1, 0, 0)]

        while len(heap) > 0:
            for _ in range(len(heap)):
                dist, row, col = heappop(heap)

                if (row == (len(grid) - 1) and col == (len(grid) - 1)):
                    return dist

                for dr, dc in neighbours:
                    n_row = row + dr
                    n_col = col + dc

                    if ((n_row < 0 or n_row >= len(grid)) or 
                        (n_col < 0 or n_col >= len(grid)) or 
                        ((n_row, n_col) in visit) or
                        (grid[n_row][n_col] == 1)):
                        continue
                    
                    visit.add((n_row, n_col))
                    heappush(heap, (dist + 1, n_row, n_col))
        
        return -1
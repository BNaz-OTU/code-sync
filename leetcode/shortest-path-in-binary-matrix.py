class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if (grid[0][0] == 1 or grid[-1][-1] == 1):
            return -1
        
        heap = []
        heap.append([1, 0, 0])
        visit = set()
        neighbour = [[1, 0], [0, 1], [-1, 0], [0, -1], [-1, -1], [1, 1], [-1, 1], [1, -1]]

        while len(heap) > 0:
            dist, row, col = heappop(heap)

            if (row == (len(grid) - 1) and col == (len(grid) - 1)):
                return dist

            for dr, dc in neighbour:
                n_row = dr + row
                n_col = dc + col

                if ((n_row < 0 or n_row >= len(grid)) or
                    (n_col < 0 or n_col >= len(grid)) or
                    (grid[n_row][n_col] == 1) or
                    ((n_row, n_col) in visit)):
                    continue
                
                heappush(heap, [dist + 1, n_row, n_col])
                visit.add((n_row, n_col))
        
        return -1
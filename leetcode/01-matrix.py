class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(mat), len(mat[0])
        queue = deque()
        visit = set()
        dist = 1
        neighbors = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        for row in range(ROWS):
            for col in range(COLS):
                if (mat[row][col] == 0):
                    queue.append((row, col))
                    visit.add((row, col))
        
        while len(queue) > 0:

            for _ in range(len(queue)):
                row, col = queue.popleft()

                for dr, dc in neighbors:
                    n_row = row + dr
                    n_col = col + dc

                    if ((n_row < 0 or n_row >= ROWS) or
                        (n_col < 0 or n_col >= COLS) or
                        ((n_row, n_col) in visit)):
                        continue
                    
                    mat[n_row][n_col] = dist
                    visit.add((n_row, n_col))
                    queue.append((n_row, n_col))

            dist += 1
        
        return mat
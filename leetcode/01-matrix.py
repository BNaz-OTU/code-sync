class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(mat), len(mat[0])
        queue = deque()
        visit = set()
        neighbours = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        for row in range(ROWS):
            for col in range(COLS):
                if (mat[row][col] == 0):
                    queue.append([row, col])
                    visit.add((row, col))
        
        count = 1
        while len(queue) > 0:
            print(queue)
            for _ in range(len(queue)):
                row, col = queue.popleft()

                for dr, dc in neighbours:
                    n_row = row + dr
                    n_col = col + dc

                    if ((n_row < 0 or n_row >= ROWS) or
                        (n_col < 0 or n_col >= COLS) or
                        ((n_row, n_col) in visit)):
                        # print("h")
                        continue
                    
                    visit.add((n_row, n_col))
                    queue.append([n_row, n_col])
                    mat[n_row][n_col] = count
            
            count += 1
        
        return mat
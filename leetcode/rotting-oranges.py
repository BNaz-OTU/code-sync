class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        freshCount = 0
        neighbors = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        for row in range(ROWS):
            for col in range(COLS):
                if (grid[row][col] == 1):
                    freshCount += 1
                
                elif (grid[row][col] == 2):
                    queue.append((row, col))
        
        if freshCount == 0:
            return 0
        
        time = 0
        while len(queue) > 0:
            if freshCount == 0:
                return time
            
            search = len(queue)
            time += 1

            for _ in range(search):
                x, y = queue.popleft()

                for dr, dc in neighbors:
                    new_x, new_y = x + dr, y + dc
                    
                    if ((new_x >= 0 and new_x < ROWS) and
                        (new_y >= 0 and new_y < COLS) and
                        (grid[new_x][new_y] == 1)):
                        grid[new_x][new_y] = 2
                        freshCount -= 1
                        queue.append((new_x, new_y))
                
        if (freshCount != 0):
            return -1
        else:
            return time
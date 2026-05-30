class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        target = image[sr][sc]
        ROWS, COLS = len(image), len(image[0])
        visit = set()

        def dfs(row, col):
            if ((row < 0 or row >= ROWS) or
                (col < 0 or col >= COLS) or
                (image[row][col] != target) or
                ((row, col) in visit)):
                return 
            
            image[row][col] = color
            visit.add((row, col))

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        
        dfs(sr, sc)
        return image
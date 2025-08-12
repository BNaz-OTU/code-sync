class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # USED SOLN: https://www.youtube.com/watch?v=iIMHsGZRIOE
        
        dict_row = defaultdict(int)
        pairs = 0
        n = len(grid)

        for row in grid:
            dict_row[tuple(row)] += 1
        
        for col in range(n):
            column = tuple(grid[r][col] for r in range(n))
            if column in dict_row:
                pairs += dict_row[column]
        return pairs
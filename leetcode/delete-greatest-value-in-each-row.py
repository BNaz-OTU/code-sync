class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        final = 0

        for idx in range(len(grid)):
            for jdx in range(len(grid[idx])):
                grid[idx][jdx] = grid[idx][jdx] * -1
        
        print(grid)

        while len(grid[0]) > 0:
            deleteList = []
            for idx in range(len(grid)):
                # arr = grid[idx]
                heapify(grid[idx])
                val = heappop(grid[idx])
                deleteList.append(val)
                
            final += min(deleteList)
        
        return final * -1
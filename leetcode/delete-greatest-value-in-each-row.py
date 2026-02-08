class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        finalsum = 0
        for idx in range(len(grid)):
            for kdx in range(len(grid[idx])):
                grid[idx][kdx] = grid[idx][kdx] * -1
                
        while (len(grid[0]) > 0):
            deleted = []
            for idx in range(len(grid)):
                heapify(grid[idx])
                deleted.append(heappop(grid[idx]))
            finalsum += min(deleted) * -1 
        
        return finalsum
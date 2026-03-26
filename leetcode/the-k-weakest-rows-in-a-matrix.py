class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        final = []
        for row in range(len(mat)):
            row_count = 0
            for col in range(len(mat[0])):
                if (mat[row][col] == 0):
                    break
                row_count += 1
            
            heap.append([row_count, row])
        
        print(heap)

        heapify(heap)

        while len(final) != k:
            _, num = heappop(heap)
            final.append(num)
        
        return final
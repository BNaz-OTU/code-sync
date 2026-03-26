class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        final = []
        heap = []
        
        for row in range(len(mat)):
            count = 0
            for col in range(len(mat[0])):
                if (mat[row][col] == 1):
                    count += 1
            heap.append([count, row])
        
        heapify(heap)

        while len(final) != k:
            print(heap)
            _, n = heappop(heap)
            final.append(n)
        return final
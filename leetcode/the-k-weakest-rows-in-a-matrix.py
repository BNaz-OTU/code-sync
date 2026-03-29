class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        final = []

        for idx in range(len(mat)):
            count = 0
            for jdx in range(len(mat[idx])):
                if (mat[idx][jdx] == 0):
                    break
                count += 1
            heap.append([count, idx])
        
        heapify(heap)

        while len(final) != k:
            val = heappop(heap)
            final.append(val[1])
        
        return final
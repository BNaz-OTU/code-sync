class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        final = []
        
        for x, y in points:
            val = math.sqrt(((x - 0) ** 2) + ((y - 0) ** 2))
            heap.append([val, x, y])
        
        heapify(heap)
        while len(final) != k:
            _, x, y = heappop(heap)
            final.append([x, y])
        
        return final
        print(heap)
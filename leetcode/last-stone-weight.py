class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heap.append(stone * -1)
        
        heapify(heap)
        while len(heap) > 1:
            val1 = heappop(heap) * -1
            val2 = heappop(heap) * -1
            calc = abs(val1 - val2)

            if (calc == 0):
                continue
            else:
                heap.append(calc * -1)
        
        if (len(heap) == 0):
            return 0
            
        return heap[0] * -1
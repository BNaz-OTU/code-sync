class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heap = []

        for stone in stones:
            heappush(heap, -stone)

        while len(heap) > 1:
            val1 = heappop(heap)
            val2 = heappop(heap)

            if (val1 != val2):
                heappush(heap, abs((val1 * -1) - (val2 * -1)) * -1)
            
        return heap[0] * -1 if len(heap) > 0 else 0
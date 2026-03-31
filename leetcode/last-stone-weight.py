class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        for stone in stones:
            heap.append(stone * -1)
        
        heapify(heap)

        while len(heap) > 1:
            val1 = heappop(heap) * -1
            val2 = heappop(heap) * -1

            smash = abs(val1 - val2)

            if (smash == 0):
                continue
            else:
                heappush(heap, smash * -1)
        
        if (len(heap) != 0):
            return heap[0] * -1
        else:
            return 0
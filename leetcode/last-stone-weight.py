class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for idx in range(len(stones)):
            stones[idx] = stones[idx] * -1
        
        heapq.heapify(stones)

        while len(stones) > 1:
            val1 = heapq.heappop(stones) * -1
            val2 = heapq.heappop(stones) * -1

            diff = val1 - val2

            if (diff > 0):
                heapq.heappush(stones, diff * -1)
        
        if (len(stones) == 1):
            return stones[0] * -1
        
        return 0
class Solution:
    # USED SOLN: https://www.youtube.com/watch?v=B-QCq79-Vfw
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Since python is dumb and can't implement a max heap, convert numbers to negative to get the "max heap" effect 
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if (second > first):
                heapq.heappush(stones, first - second)
        
        stones.append(0)
        return abs(stones[0])
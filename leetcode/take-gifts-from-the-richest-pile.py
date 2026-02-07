import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        for idx in range(len(gifts)):
            gifts[idx] = gifts[idx] * -1
        
        heapify(gifts)

        while k > 0:
            k -= 1
            
            # Extract value
            val = heappop(gifts)

            # Conduct Operations
            val = val * -1
            val = math.sqrt(val)
            val = math.floor(val) * -1
            
            heappush(gifts, val)
        
        return sum(gifts) * -1
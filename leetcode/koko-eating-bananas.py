import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        final = right

        while left <= right:
            middle = (left + right) // 2
            count = 0

            for pile in piles:
                count += math.ceil(pile / middle)
            
            print(middle, count)
            if (count <= h):
                final = min(final, middle)
                right = middle - 1

            else:            
                left = middle + 1
        
        return final
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        minTime = 0

        while left <= right:
            middle = (left + right) // 2

            count = 0
            for pile in piles:
                count += math.ceil(pile / middle)
            
            print(f"Left: {left} | Right: {right} | Middle: {middle} | Time: {count}")
            
            if (count > h):
                left = middle + 1
            
            elif (count <= h):
                minTime = middle
                right = middle - 1
        
        return minTime
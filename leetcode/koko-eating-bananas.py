class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        finalSpeed = max(piles)

        while left <= right:
            speed = (left + right) // 2
            time = 0

            for pile in piles:
                time += math.ceil(pile / speed)
            
            if (time > h):
                left = speed + 1
            
            else:
                right = speed - 1
                finalSpeed = min(finalSpeed, speed)
        
        return finalSpeed
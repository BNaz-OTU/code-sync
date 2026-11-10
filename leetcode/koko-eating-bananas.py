import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles)
        maxTime = 0
        eat = 0

        while left <= right:
            eat_speed = (left + right) // 2
            time = 0

            for pile in piles:
                time += math.ceil(pile / eat_speed)

            print(eat_speed, time)
            if (time > h):
                left = eat_speed + 1
            
            else:
                if (time >= maxTime):
                    maxTime = time
                    eat = eat_speed

                right = eat_speed - 1
        
        return eat
import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles)
        maxSpeed = float("infinity")

        while left <= right:
            eat_speed = (left + right) // 2
            time = 0
            for pile in piles:
                time += math.ceil(pile / eat_speed)

            # print(f"EAT Speed: {eat_speed} | TIME to EAT: {time}")
            if (time > h):
                left = eat_speed + 1
            
            else:
                right = eat_speed - 1
                maxSpeed = min(maxSpeed, eat_speed)
            
        return maxSpeed
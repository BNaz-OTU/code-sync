class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # USED SOLN: https://www.youtube.com/watch?v=U2SozAs9RzA

        sort_pile = sorted(piles)
        final = sort_pile[-1]

        if (len(piles) == h):
            return sort_pile[-1]
        
        left = 1
        right = sort_pile[-1]

        while (left <= right):
            middle = (left + right) // 2
            print(f"Left: {left} | Right: {right} | Middle: {middle}")
            count = 0

            for val in piles:
                count += math.ceil(val / middle)
            
            if (count <= h):
                final = min(final, middle)
                right = middle - 1

            else:
                left = middle + 1
        
        return final

        # [3,6,7,11] / 8 = 3.375
        # [30,11,23,4,20] / 6 = 14.6666666667
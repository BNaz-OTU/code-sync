# import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        final = []

        for x, y in points:
            x_val = abs(x) ** 2
            y_val = abs(y) ** 2

            final_val = (x_val + y_val) ** 0.5
            heappush(heap, [final_val, x, y])
            
        while k > 0:
            _, x, y = heappop(heap)
            final.append([x, y])
            k -= 1
        
        return final
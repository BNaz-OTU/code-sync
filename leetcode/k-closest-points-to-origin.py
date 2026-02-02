import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        final = []
        answer = []

        for point in points:
            x, y = point
            ans = math.sqrt(((x - 0) ** 2) + ((y - 0) ** 2))
            print(x, y, ans)
            heappush(final, [ans, point])
        
        print(final)

        while k > 0:
            useless, coords = heappop(final)
            print(useless, coords)
            answer.append(coords)
            k-= 1
        
        return answer
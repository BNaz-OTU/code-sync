class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        colorList = [0] * n
        final = []

        count = 0
        for idx, color in queries:
            prev = colorList[idx - 1] if idx > 0 else 0
            nxt = colorList[idx + 1] if idx < n - 1 else 0

            if ((colorList[idx] != 0) and (colorList[idx] == prev)):
                count -= 1
            
            if ((colorList[idx] != 0) and (colorList[idx] == nxt)):
                count -= 1
            
            colorList[idx] = color

            if ((colorList[idx] != 0) and (colorList[idx] == prev)):
                count += 1
            
            if ((colorList[idx] != 0) and (colorList[idx] == nxt)):
                count += 1

            final.append(count)
        
        return final
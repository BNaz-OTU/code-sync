class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        colorList = [0] * n
        final = []
        count = 0

        for position, color in queries:
            if ((position - 1) >= 0 and (colorList[position] == colorList[position - 1]) and colorList[position] != 0):
                count -= 1
            
            if ((position + 1) < len(colorList) and (colorList[position] == colorList[position + 1]) and colorList[position] != 0):
                count -= 1
                
            colorList[position] = color

            if ((position - 1) >= 0 and (colorList[position] == colorList[position - 1]) and colorList[position] != 0):
                count += 1
            
            if ((position + 1) < len(colorList) and (colorList[position] == colorList[position + 1]) and colorList[position] != 0):
                count += 1

            final.append(count)
            # print(colorList)
            # print(final)

        return final
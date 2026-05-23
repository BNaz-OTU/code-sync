class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        colorList = [0] * n
        counter = 0
        final = []

        for position, color in queries:
            if ((position - 1 >= 0) and (colorList[position] != 0) and (colorList[position] == colorList[position - 1])):
                counter -= 1
            
            if ((position + 1 < len(colorList)) and (colorList[position] != 0) and (colorList[position] == colorList[position + 1])):
                counter -= 1
            
            colorList[position] = color

            if ((position - 1 >= 0) and (colorList[position] != 0) and (colorList[position] == colorList[position - 1])):
                counter += 1
            
            if ((position + 1 < len(colorList)) and (colorList[position] != 0) and (colorList[position] == colorList[position + 1])):
                counter += 1
            

            final.append(counter)
        
        return final
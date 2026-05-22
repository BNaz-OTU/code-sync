class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        top, bot = 0, n
        left, right = 0, n
        
        # Initialize final list to hold all the values
        final = []
        for idx in range(n):
            final.append([0] * n)
        
        counter = 1
        while top < bot and left < right:
            for idx in range(left, right):
                final[top][idx] = counter
                counter += 1
            
            top += 1

            for idx in range(top, bot):
                final[idx][right - 1] = counter
                counter += 1
            
            right -= 1

            if (top >= bot or left >= right):
                return final

            for idx in range(right - 1, left - 1, -1):
                final[bot - 1][idx] = counter
                counter += 1
            
            bot -= 1

            for idx in range(bot - 1, top - 1, -1):
                final[idx][left] = counter 
                counter += 1
            
            left += 1

        return final
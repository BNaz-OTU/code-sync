class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        top, bot = 0, n
        left, right = 0, n
        
        matrix = []
        for _ in range(n):
            matrix.append([0] * n)
        
        counter = 1
        while top < bot and left < right:
            for idx in range(left, right):
                matrix[top][idx] = counter
                counter += 1
            
            top += 1

            for idx in range(top, bot):
                matrix[idx][right - 1] = counter
                counter += 1
            
            right -= 1

            for idx in range(right - 1, left - 1, -1):
                matrix[bot - 1][idx] = counter
                counter += 1
            
            bot -= 1

            for idx in range(bot - 1, top - 1, -1):
                matrix[idx][left] = counter
                counter += 1
            
            left += 1
        
        return matrix
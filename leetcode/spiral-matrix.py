class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        final = []
        left, right = 0, len(matrix[0])
        top, bot = 0, len(matrix)

        while top < bot and left < right:
            for idx in range(left, right):
                final.append(matrix[top][idx])
            
            top += 1
            for jdx in range(top, bot):
                final.append(matrix[jdx][right - 1])
            
            right -= 1
            if not(left < right and top < bot):
                return final
                
            for wdx in range(right - 1, left - 1, -1):
                final.append(matrix[bot - 1][wdx])
            

            bot -= 1
            for zdx in range(bot - 1, top - 1, -1):
                final.append(matrix[zdx][left])

            left += 1        
        return final
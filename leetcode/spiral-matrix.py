class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        final = []
        left, right = 0, len(matrix[0])
        top, bot = 0, len(matrix)

        while top < bot and left < right:
            for idx in range(left, right):
                final.append(matrix[top][idx])
            
            top += 1

            for idx in range(top, bot):
                final.append(matrix[idx][right - 1])
            
            right -= 1

            # print(f"Top: {top} | Bot: {bot} | Right: {right} | Left: {left}")
            if (top >= bot or left >= right):
                return final

            for idx in range(right - 1, left - 1, -1):
                final.append(matrix[bot - 1][idx])
            
            bot -= 1

            for idx in range(bot - 1, top - 1, -1):
                final.append(matrix[idx][left])
            
            left += 1

        return final
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        top, bot = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top < bot and left < right:

            for idx in range(right - left):
                topLeftTemp = matrix[top][left + idx]

                matrix[top][left + idx] = matrix[bot - idx][left]

                matrix[bot - idx][left] = matrix[bot][right - idx]

                matrix[bot][right - idx] = matrix[top + idx][right]

                matrix[top + idx][right] = topLeftTemp
        
            left += 1
            top += 1
            right -= 1
            bot -= 1

        return matrix
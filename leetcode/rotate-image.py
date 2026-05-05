class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        top, bot = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top < bot and left < right:
            for idx in range(right - left):
                tempVal = matrix[top][left + idx]

                # Change Top-left row
                matrix[top][left + idx] = matrix[bot - idx][left]

                # Change Bottom-left column
                matrix[bot - idx][left] = matrix[bot][right - idx]

                # Change Bottom-right column
                matrix[bot][right - idx] = matrix[top + idx][right]

                # Change Top-right row
                matrix[top + idx][right] = tempVal
            
            top += 1
            bot -= 1
            left += 1
            right -= 1
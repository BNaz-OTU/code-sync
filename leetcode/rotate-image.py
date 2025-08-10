class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # USED SOLN: https://www.youtube.com/watch?v=fMSJSS7eO1w
        left, right = 0, len(matrix) - 1

        while left < right:
            for idx in range (right - left):

                top, bottom = left, right
                
                # Save the top-left value
                tempTopLeft = matrix[top][left + idx]

                # Move bottom left into top left
                matrix[top][left + idx] = matrix[bottom - idx][left]

                # Move bottom right into bottom left
                matrix[bottom - idx][left] = matrix[bottom][right - idx]

                # Move top right into bottom right
                matrix[bottom][right - idx] = matrix[top + idx][right]

                # Move top left into top right
                matrix[top + idx][right] = tempTopLeft
            right -= 1
            left += 1
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # SOLVED BY MYSELF
        # SOLN VID FOR REFERENCE: https://www.youtube.com/watch?v=UuiTKBwPgAo
        left = 0
        right = len(height) - 1
        maxWater = 0

        while left < right:
            # I'm forced to choose the smaller height, otherwise choosing the
            # smaller bigger height leak out some water/go against the rule of
            # "no slanting the container" 
            minHeight = min(height[left], height[right])
            width = right - left

            # Update everytime there is a new area that can take more water
            maxWater = max((minHeight * width), maxWater)

            # Update the smaller height to hopefully get a bigger height value
            if (height[left] < height[right]):
                left += 1
            else:
                right -= 1
        
        return maxWater
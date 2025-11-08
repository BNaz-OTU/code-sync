class Solution:
    def trap(self, height: List[int]) -> int:

        # USED SOLN: https://www.youtube.com/watch?v=ZI2z5pq0TqA

        if (len(height) == 0):
            return 0
        
        left, right = 0, len(height) - 1
        leftMax, rightMax = height[left], height[right]
        final = 0

        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                final += leftMax - height[left]

            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                final += rightMax - height[right]
        
        return final
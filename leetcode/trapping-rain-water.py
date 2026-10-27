class Solution:
    def trap(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        maxLeft, maxRight = height[left], height[right]
        water = 0

        while left < right:
            if maxLeft > maxRight:
                right -= 1
                maxRight = max(maxRight, height[right])
                water += maxRight - height[right]
            
            else:
                left += 1
                maxLeft = max(maxLeft, height[left])
                water += maxLeft - height[left]
        
        return water
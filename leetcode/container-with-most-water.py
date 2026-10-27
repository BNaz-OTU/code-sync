class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        maxHeight = 0

        # print(height[0])

        while left < right:
            width = right - left
            w_height = min(height[left], height[right])
            maxHeight = max(maxHeight, width * w_height)


            if (height[right] >= height[left]):
                left += 1
            else:
                right -= 1
        
        return maxHeight
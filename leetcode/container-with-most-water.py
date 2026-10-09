class Solution:
    def maxArea(self, height: list[int]) -> int:
        water = 0
        left, right = 0, len(height) - 1

        while left < right:
            lWall, rWall = height[left], height[right]
            cheight = min(lWall, rWall)

            water = max(water, cheight * (right - left))
            # print(f"Height: {cheight} | leftWall: {lWall} | rightWall: {rWall}\n\tleft:{left} | right:{right} | width: {right - left + 1} | water: {water}")
            # print("-" * 30)

            if (rWall <= lWall):
                right -= 1
            
            else:
                left += 1

        return water
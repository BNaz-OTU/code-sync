class Solution:
    def jump(self, nums: List[int]) -> int:
        # USED SOLN: https://www.youtube.com/watch?v=dJ7sWiOoK7g
        res = 0
        left, right = 0, 0

        while right < len(nums) - 1:
            farthest = 0
            for idx in range(left, right + 1):
                farthest = max(farthest, idx + nums[idx])
            
            left = right + 1
            right = farthest
            res += 1

        return res
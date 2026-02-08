class Solution:
    # USED SOLN: https://www.youtube.com/watch?v=Yan0cv2cLy8
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for idx in range(len(nums) - 1, -1, -1):
            if (idx + nums[idx] >= goal):
                goal = idx
        
        return True if goal == 0 else False
class Solution:
    def rob(self, nums: List[int]) -> int:
        if (len(nums) < 2):
            return max(nums)
        
        dp = 0
        for idx in range(2, len(nums)):
            nums[idx] = max(nums[idx], nums[idx] + nums[idx - 2], nums[idx] + dp)
            dp = nums[idx - 2]
        
        return max(nums[-1], nums[-2])
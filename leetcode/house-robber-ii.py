class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            dp = [0, nums[0]]
            for idx in range(2, len(nums)):
                nums[idx] = max(nums[idx], nums[idx] + dp[1], nums[idx] + dp[0])
                dp[0] = dp[1]
                dp[1] = nums[idx - 1]
            
            return max(nums[-1], nums[-2])
        
        if (len(nums) <= 2):
            return max(nums)

        val = max(helper(nums[1:]), helper(nums[:len(nums) - 1]))

        return val
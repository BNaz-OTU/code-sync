class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # USED SOLN: https://www.youtube.com/watch?v=bNvIQI2wAjk
        new_list = [1] * len(nums)
        prefix = 1
        postfix = 1

        for idx in range(len(nums)):
            new_list[idx] = prefix
            prefix *= nums[idx]

        for idx in range(len(nums) - 1, -1, -1):
            new_list[idx] *= postfix
            postfix *= nums[idx]

        return new_list
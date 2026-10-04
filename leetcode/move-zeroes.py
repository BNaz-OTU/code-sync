class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in range(len(nums)):
            while left < right and nums[left] != 0:
                left += 1
            
            if (nums[right] != 0):
                nums[left], nums[right] = nums[right], nums[left]
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        for right in range(len(nums)):
                
            if (left < len(nums) and nums[left] == 0 and nums[right] != 0):
                nums[left] = nums[right]
                nums[right] = 0

            while left < right and nums[left] != 0:
                left += 1
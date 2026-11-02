class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if middle > 0  and nums[middle] < nums[middle - 1]:
                right = middle - 1

            elif middle < len(nums) - 1 and nums[middle] < nums[middle + 1]:
                left = middle + 1
            
            else:
                return middle
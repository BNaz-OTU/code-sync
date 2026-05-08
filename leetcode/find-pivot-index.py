class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for idx in range(len(nums)):
            left = sum(nums[:idx])
            right = sum(nums[idx + 1:])

            if (left == right):
                return idx
        
        return -1
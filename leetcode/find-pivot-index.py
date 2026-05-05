class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        for idx in range(len(nums)):
            sumRight = sum(nums[idx + 1:])
            sumLeft = sum(nums[:idx])

            if (sumRight == sumLeft):
                return idx
        
        return -1
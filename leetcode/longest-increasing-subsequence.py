class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        LIS = [1] * len(nums)

        for idx in range(len(nums) - 1, -1, -1):
            for j in range(idx + 1, len(nums)):
                if nums[idx] < nums[j]:
                    LIS[idx] = max(LIS[idx], 1 + LIS[j])
        
        return max(LIS)
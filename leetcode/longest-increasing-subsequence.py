class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        checker = [1] * len(nums)

        for idx in range(len(nums) - 1, -1, -1):
            for jdx in range(idx, len(nums)):
                if (nums[idx] < nums[jdx]):
                    checker[idx] = max(checker[idx], 1 + checker[jdx])
        
        return max(checker)
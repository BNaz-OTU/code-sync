class Solution:
    def rob(self, nums: list[int]) -> int:
        nums.append(0)

        for idx in range(len(nums) - 4, -1, -1):
            nums[idx] += max(nums[idx + 2], nums[idx + 3])
        
        return max(nums[0], nums[1])
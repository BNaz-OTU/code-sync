class Solution:
    def rob(self, nums: List[int]) -> int:

        if (len(nums) < 2):
            return max(nums)
        
        new_nums = [0, 0] + nums
        
        for idx in range(3, len(new_nums)):
            new_nums[idx] = max(new_nums[idx] + new_nums[idx - 2], new_nums[idx] + new_nums[idx - 3])
        
        print(new_nums)
        return max(new_nums[-1], new_nums[-2])
class Solution:
    def rob(self, nums: list[int]) -> int:
        
        def helper(nums):
            nums.append(0)

            for idx in range(len(nums) - 4, -1, -1):
                nums[idx] += max(nums[idx + 2], nums[idx + 3])
            
            return max(nums[0], nums[1])
        
        if (len(nums) == 1):
            return nums[0]

        return max(helper(nums[1:]), helper(nums[:-1]))
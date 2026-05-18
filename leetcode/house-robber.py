class Solution:
    def rob(self, nums: List[int]) -> int:
        profit = [0, nums[0]]

        for idx in range(2, len(nums)):
            nums[idx] += max(profit[0], profit[1])
            profit[0] = profit[1]
            profit[1] = nums[idx - 1]
        
        print(nums)
        return max(max(profit), nums[len(nums) - 1])
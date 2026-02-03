class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if (len(nums) == 2):
            return (nums[0] - 1) * (nums[1] - 1)

        for idx in range(len(nums)):
            nums[idx] = nums[idx] * -1
        
        heapify(nums)

        num1 = heappop(nums) * -1
        num2 = heappop(nums) * -1

        return (num1 - 1) * (num2 -1)
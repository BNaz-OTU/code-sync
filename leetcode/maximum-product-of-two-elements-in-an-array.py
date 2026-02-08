class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        for idx in range(len(nums)):
            nums[idx] = nums[idx] * -1

        heapify(nums)
        val1 = heappop(nums) * -1
        val2 = heappop(nums) * -1

        return (val1 - 1) * (val2 - 1)
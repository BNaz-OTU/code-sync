class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final = []

        prefix = 1
        for num in nums:
            final.append(prefix)
            prefix *= num
        
        suffix = 1
        for idx in range(len(nums) - 1, -1, -1):
            final[idx] *= suffix
            suffix *= nums[idx]

        return final
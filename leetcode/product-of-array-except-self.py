class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = [1] * (len(nums) + 1)
        suffix = [1] * (len(nums) + 1)
        final = []

        for idx in range(len(nums)):
            prefix[idx + 1] = nums[idx] * prefix[idx]
        
        for idx in range(len(nums) - 1, -1, -1):
            suffix[idx] = nums[idx] * suffix[idx + 1]
        
        for idx in range(1, len(suffix)):
            final.append(prefix[idx -1] * suffix[idx])
        
        return final
        

        
        print(prefix)
        print(suffix)
        # [1, 1, 2, 6, 24]
        # [24, 24, 12, 4, 1]
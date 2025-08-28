class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        final = []

        for idx in range(1, len(nums)):
            prefix[idx] = prefix[idx - 1] * nums[idx - 1]
        
        for idx in range(len(nums) - 2, -1, -1):
            suffix[idx] = suffix[idx + 1] * nums[idx + 1]

        for idx in range(len(nums)):
            final.append(prefix[idx] * suffix[idx])
        
        print(final)
        return final

        
        # print(prefix)
        # print(suffix)

        # [1, 2, 3, 4] [1]
        # [1, 1, 8, 6] 
        # [24, 12, 4, 1]
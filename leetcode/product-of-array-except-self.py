class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        pre1 = [1] * (len(nums) + 1)
        pre2 = [1] * (len(nums) + 1)
        final = []

        #   1 2 3 4
        # 1 1 2 6 24

        # 1 2 3 4
        # 24 24 12 4 1

        for idx in range(len(nums)):
            pre1[idx + 1] = pre1[idx] * nums[idx]
        
        rev_nums = nums[::-1]
        
        for idx in range(len(rev_nums)):
            pre2[idx + 1] = pre2[idx] * rev_nums[idx]
        
        rev_pre2 = pre2[::-1]

        for idx in range(1, len(nums) + 1):
            final.append(pre1[idx - 1] * rev_pre2[idx])
        
        return final
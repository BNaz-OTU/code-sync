class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * (len(nums) * 2)

        for idx in range(len(nums)):
            ans[idx] = nums[idx]
            ans[idx + len(nums)] = nums[idx]
        
        return ans
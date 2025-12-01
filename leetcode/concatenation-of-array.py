class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums[:]

        for idx in range(len(nums)):
            ans.append(nums[idx])

        return ans
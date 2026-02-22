class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        maxNum = max(nums)
        final = 0

        for _ in range(k):
            final += maxNum
            maxNum += 1
        
        return final
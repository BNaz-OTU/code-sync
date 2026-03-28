class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxCount = 0

        for num in numSet:
            if (num - 1 in numSet):
                continue
            else: 
                count = 0
                while num in numSet:
                    num += 1
                    count += 1
                maxCount = max(count, maxCount)
        
        return maxCount
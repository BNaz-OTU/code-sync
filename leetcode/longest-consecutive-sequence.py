class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLen = 0

        for val in numSet:
            if (val - 1) not in numSet:
                counter = 0
                while (val + counter) in numSet:
                    counter += 1
                maxLen = max(maxLen, counter)
        
        return maxLen
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # USED SOLN: https://www.youtube.com/watch?v=P6RZZMu_maU
        numSet = set(nums)

        longest = 0

        for n in numSet:
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        
        return longest
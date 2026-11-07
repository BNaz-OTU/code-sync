class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                temp = num
                count = 0

                while temp in numSet:
                    count += 1
                    temp += 1
                
                longest = max(longest, count)
        
        return longest
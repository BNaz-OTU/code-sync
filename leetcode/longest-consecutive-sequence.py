class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        set_nums = set(nums)
        maxCount = 0

        for num in set_nums:
            if (num - 1 not in set_nums):
                count = 0
                temp = num
                while temp in set_nums:
                    count += 1
                    temp += 1
                maxCount = max(maxCount, count)
        
        return maxCount
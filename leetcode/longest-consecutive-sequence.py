class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visit = set(nums)
        maxCount = 0

        for num in visit:
            if ((num - 1) not in visit):
                count = 0

                while (count + num) in visit:
                    count += 1
                maxCount = max(maxCount, count)

        return maxCount
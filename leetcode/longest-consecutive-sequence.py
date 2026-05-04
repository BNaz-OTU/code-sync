class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visit = set(nums)
        maxLen = 0

        for num in visit:
            if (num - 1 not in visit):
                count = 0
                while (num + count) in visit:
                    count += 1
                
                maxLen = max(maxLen, count)
        
        return maxLen
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visit = set(nums)
        maxCount = 0

        for val in visit:
            if (val - 1) in visit:
                continue
            
            else:
                count = 0
                while (val + count) in visit:
                    count += 1
                
                maxCount = max(maxCount, count)
        
        return maxCount
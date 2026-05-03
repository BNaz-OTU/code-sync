class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        visit = set(nums)
        maxCount = 0

        for num in visit:
            if ((num - 1) not in visit):
                count = 0

                for idx in range(len(visit)):
                    if ((num + idx) in visit):
                        count += 1
                    else:
                        break
                maxCount = max(maxCount, count)

        return maxCount

            
            # visit.add(num)
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        sort_nums = sorted(nums)
        slow = 0
        fast = 1
        count = 0
        maxCount = 0

        while (fast < len(nums)):
            print(fast, sort_nums[fast], sort_nums[slow])
            if (abs(sort_nums[fast] - sort_nums[slow]) == 1):
                count = (fast - slow) + 1
                maxCount = max(maxCount, count)
                fast += 1

            elif (abs(sort_nums[fast] - sort_nums[slow]) > 1):
                slow += 1
            
            else:
                fast += 1
        
        return maxCount
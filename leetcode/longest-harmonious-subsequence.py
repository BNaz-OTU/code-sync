class Solution:
    def findLHS(self, nums: List[int]) -> int:
        fast = 1
        slow = 0
        nums = sorted(nums)

        maxCount = 0

        while fast < len(nums):
            # print(nums)
            # print(slow)
            # print(fast)
            # print("-----")
            if (abs(nums[fast] - nums[slow]) > 1):
                slow += 1
            
            elif (abs(nums[fast] - nums[slow]) == 1):
                maxCount = max(maxCount, (fast - slow) + 1)
                fast += 1

            else:
                fast += 1
        
        return maxCount
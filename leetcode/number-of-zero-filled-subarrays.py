class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        streak = 0
        counter = 0
        for index in range(len(nums)):
            if (nums[index] == 0 and streak == 0):
                counter += 1
                streak = 1
            elif (nums[index] == 0 and streak > 0):
                streak += 1
                counter += streak
            else:
                streak = 0
        
        return counter
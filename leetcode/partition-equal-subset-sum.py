class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        if (sum(nums) % 2 == 1):
            return False
        
        target = sum(nums) // 2

        dp = {0}

        for idx in range(len(nums)):
            nextDP = set()

            for val in dp:
                nextDP.add(nums[idx] + val)
                nextDP.add(nums[idx])
                nextDP.add(val)
            
            dp = nextDP
        
        return True if target in dp else False
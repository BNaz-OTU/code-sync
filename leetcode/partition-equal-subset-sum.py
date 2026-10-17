class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        if (sum(nums) % 2):
            return False
        
        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for idx in range(len(nums)):
            nextDP = set()
            for t in dp:
                nextDP.add(t)
                nextDP.add(t + nums[idx])
        
            dp = nextDP
        
        return True if target in dp else False
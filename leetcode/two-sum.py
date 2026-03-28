class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashNum = {}

        for idx in range(len(nums)):
            val = target - nums[idx]

            if (val in hashNum):
                return [hashNum[val], idx]
            
            else:
                hashNum[nums[idx]] = idx
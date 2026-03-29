class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for idx in range(len(nums)):
            val = target - nums[idx]

            if (val in hashMap):
                return [hashMap[val], idx]
            
            else:
                hashMap[nums[idx]] = idx
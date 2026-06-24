class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for idx, value in enumerate(nums):
            if ((target - value) in hashMap):
                return [hashMap[target - value], idx]
            
            hashMap[value] = idx
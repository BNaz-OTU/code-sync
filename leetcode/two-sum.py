class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        
        for idx, val in enumerate(nums):
            if ((target - val) in hashMap):
                return [hashMap[target - val], idx]
            
            hashMap[val] = idx
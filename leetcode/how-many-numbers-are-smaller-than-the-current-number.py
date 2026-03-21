class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sizeMap = {}

        for idx in range(len(nums)):
            sizeMap[idx] = 0
        
        for key in sizeMap:
            val = nums[key]
            for num in nums:
                if (val > num):
                    sizeMap[key] += 1
        
        return list(sizeMap.values())
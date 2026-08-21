class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sumVal = 0
        left = 0
        minSize = float('inf')

        for right in range(len(nums)):
            sumVal += nums[right]

            while sumVal >= target:
                minSize = min(minSize, right - left + 1)
                sumVal -= nums[left]
                left += 1
        
        return 0 if minSize == float('inf') else minSize
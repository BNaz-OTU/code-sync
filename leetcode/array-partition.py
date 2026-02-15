class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        print(nums)
        nums.sort()
        
        max_sum = 0
        for idx in range(1, len(nums), 2):
            max_sum += min(nums[idx], nums[idx - 1])
        
        return max_sum
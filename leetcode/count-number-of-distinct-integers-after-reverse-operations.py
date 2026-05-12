class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        for idx in range(len(nums)):
            val = nums[idx]
            update_val = int(str(val)[::-1])
            nums.append(update_val)
        
        return len(set(nums))
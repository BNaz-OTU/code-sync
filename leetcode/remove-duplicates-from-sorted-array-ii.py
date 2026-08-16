class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right = 0, 0

        while right < len(nums):
            count = 1

            while right + 1 < len(nums) and nums[right] == nums[right + 1]:
                right += 1
                count += 1
            
            for _ in range(min(count, 2)):
                nums[left] = nums[right]
                left += 1

            right += 1
        
        return left
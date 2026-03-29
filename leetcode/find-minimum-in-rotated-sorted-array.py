class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        minNum = nums[0]

        while left <= right:
            if (nums[left] <= nums[right]):
                minNum = min(minNum, nums[left])
            
            middle = right - left

            minNum = min(minNum, nums[middle])
            if (nums[middle] > nums[right]):
                left = middle + 1
            else:
                right = middle - 1
            
        
        return minNum
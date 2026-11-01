class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if (target == nums[middle]):
                return middle

            if (nums[left] <= nums[middle]):
                if (target < nums[left] or target > nums[middle]):
                    left = middle + 1
                else:
                    right = middle
            
            else:
                if (target > nums[right] or target < nums[middle]):
                    right = middle
                
                else:
                    left = middle + 1
        
        return -1
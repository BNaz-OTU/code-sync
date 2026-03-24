# USED SOLN: https://www.youtube.com/watch?v=nIVW4P8b1VA

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        final = nums[0]


        while (left <= right):
            if (nums[left] < nums[right]):
                final = min(final, nums[left])

            middle = right - left
            print(f"Left: {nums[left]} | Right: {nums[right]} | Middle: {nums[middle]}")
            final = min(final, nums[middle])
            if (nums[middle] >= nums[left]):
                left = middle + 1
            else:
                right = middle - 1
            
        
        return final
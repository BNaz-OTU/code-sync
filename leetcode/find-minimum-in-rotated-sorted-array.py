class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            # print(f"Left: {nums[left]} | Middle: {nums[middle]} | Right: {nums[right]}")

            if (nums[left] <= nums[right]):
                return nums[left]
            
            elif (nums[left] <= nums[middle]):
                left = middle + 1
            
            else:
                right = middle
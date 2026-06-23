class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        final = []
        nums.sort()

        for idx in range(len(nums)):
            if (idx > 0 and nums[idx - 1] == nums[idx]):
                continue
            
            left = idx + 1
            right = len(nums) - 1

            while left < right:
                val1 = nums[left]
                val2 = nums[right]
                threeSum = nums[idx] + val1 + val2

                if (threeSum == 0):
                    final.append([nums[idx], val1, val2])

                    while left < right and nums[left] == val1:
                        left += 1
                
                elif (threeSum > 0):
                    right -= 1
                
                else:
                    left += 1
        
        return final
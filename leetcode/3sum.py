class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        final = []
        nums.sort()

        for idx in range(len(nums)):
            if (idx > 0 and nums[idx] == nums[idx - 1]):
                continue
            
            left = idx + 1
            right = len(nums) - 1

            while left < right:
                leftVal = nums[left]
                rightVal = nums[right] 
                threeSum = nums[idx] + leftVal + rightVal

                if (threeSum == 0):
                    final.append([nums[idx], leftVal, rightVal])

                    while left < right and leftVal == nums[left]:
                        left += 1
                
                elif (threeSum < 0):
                    left += 1
                
                else:
                    right -= 1

        return final
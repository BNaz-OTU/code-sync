class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        final = []
        nums.sort()

        for idx in range(len(nums) - 1):
            if (idx > 0 and nums[idx] == nums[idx - 1]):
                continue

            left, right = idx + 1, len(nums) - 1

            while left < right:
                if ((nums[idx] + nums[left] + nums[right]) == 0):
                    final.append([nums[idx], nums[left], nums[right]])
                    right -= 1
                    while right > left and nums[right] == nums[right + 1]:
                        right -= 1
                    
                elif ((nums[idx] + nums[left] + nums[right]) > 0):
                    right -= 1
                
                else:
                    left += 1
        
        return final
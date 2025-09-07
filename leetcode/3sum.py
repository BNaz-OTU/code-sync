class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        final = []
        print(nums)

        for idx in range(len(nums) - 1):

            if (idx > 0 and nums[idx - 1] == nums[idx]):
                continue

            left = idx + 1
            right = len(nums) - 1
            cur_sum = 0
            

            while (left < right):
                cur_sum = nums[idx] + nums[left] + nums[right]
                
                if (cur_sum > 0):
                    right -= 1
                
                elif (cur_sum < 0):
                    left += 1
                
                else:
                    final.append([nums[idx], nums[left], nums[right]])
                    left += 1

                    while (nums[left] == nums[left - 1] and left < right):
                        left += 1
        
        return final
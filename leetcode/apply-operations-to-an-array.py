class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for idx in range(len(nums) - 1):
            if (nums[idx] == nums[idx + 1]):
                nums[idx] = nums[idx] * 2
                nums[idx + 1] = 0
        
        print(nums)
        
        fast = 0
        slow = 0

        while fast < len(nums):
            if (nums[fast] == 0):
                nextv = fast
                while nextv < len(nums):
                    if (nums[nextv] != 0):
                        nums[fast], nums[nextv] = nums[nextv], nums[fast]
                        break
                    nextv += 1
            
            fast += 1

        return nums
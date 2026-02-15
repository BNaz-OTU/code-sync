class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if (len(nums) == 1):
            return 0
        
        counter = 0

        for idx in range(1, len(nums)):
            min_num = nums[idx - 1]
            cur_num = nums[idx]

            if (min_num >= cur_num):
                diff = (min_num - cur_num) + 1
                nums[idx] += diff
                counter += diff
            
        print(nums)
        return counter
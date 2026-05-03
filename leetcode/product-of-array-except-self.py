class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_left_start = [1] * (len(nums) + 1)
        nums_right_start = [1] * (len(nums) + 1)
        final = []

        count = 0
        for idx in range(len(nums)):
            count -= 1
            nums_left_start[idx + 1] = nums_left_start[idx] * nums[idx]
            nums_right_start[idx + 1] = nums_right_start[idx] * nums[count]
        
        r_nums_right_start = nums_right_start[::-1]

        for idx in range(len(nums)):
            final.append(nums_left_start[idx] * r_nums_right_start[idx + 1])
        
        return final
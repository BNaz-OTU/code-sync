class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftStart = [1] * (len(nums) + 1)
        rightStart = [1] * (len(nums) + 1)
        final = []

        count = 0
        for idx in range(len(nums)):
            count -= 1
            leftStart[idx + 1] = leftStart[idx] * nums[idx]
            rightStart[idx + 1] = rightStart[idx] * nums[count]
        
        r_rightStart = rightStart[::-1]

        for idx in range(len(nums)):
            final.append(leftStart[idx] * r_rightStart[idx + 1])
        
        return final
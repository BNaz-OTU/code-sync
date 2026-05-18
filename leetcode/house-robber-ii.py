class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) < 2:
            return max(nums)

        dp1 = [0, 0]

        for num in nums[:len(nums) - 1]:
            temp = max(num + dp1[0], dp1[1])
            dp1[0] = dp1[1]
            dp1[1] = temp
            
        dp2 = [0, nums[1]]

        for num in nums[2:]:
            temp = max(num + dp2[0], dp2[1])
            dp2[0] = dp2[1]
            dp2[1] = temp
        
        return max(max(dp1), max(dp2))
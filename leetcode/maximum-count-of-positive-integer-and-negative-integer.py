class Solution:

    # USED SOLN: https://www.youtube.com/watch?v=peDOEoJN8ls

    def maximumCount(self, nums: List[int]) -> int:
        pos = len(nums) - self.positive(nums)
        neg = self.negative(nums)
        return max(pos, neg)

    def positive(self, nums):
        left = 0
        right = len(nums) - 1
        index = len(nums)

        while left <= right:
            middle = (left + right) // 2

            if (nums[middle] <= 0):
                left = middle + 1
            else:
                right = middle - 1
                index = middle
                
        return index
    
    def negative(self, nums):
        left = 0
        right = len(nums) - 1
        index = len(nums)

        while left <= right:
            middle = (left + right) // 2

            if (nums[middle] < 0):
                left = middle + 1
            else:
                right = middle - 1
                index = middle

        return index
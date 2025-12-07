class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        set_nums = set()

        for idx in range(1, len(nums) + 1):
            set_nums.add(idx)

        for num in nums:
            if (num in set_nums):
                set_nums.remove(num)
        
        return list(set_nums)
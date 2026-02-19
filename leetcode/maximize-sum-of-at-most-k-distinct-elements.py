class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        new_nums = list(set(nums))
        new_nums.sort(reverse=True)

        return new_nums[:k]
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums2 = []

        for idx in range(n):
            nums2.append(nums[idx])
            nums2.append(nums[idx + n])

        return nums2
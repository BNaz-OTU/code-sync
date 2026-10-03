class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        new_nums = nums1 + nums2
        new_nums.sort()

        if (len(new_nums) % 2 == 1):
            index = (len(new_nums) // 2)
            return new_nums[index]
        
        if (len(new_nums) % 2 == 0):
            index1 = (len(new_nums) // 2)
            index2 = (len(new_nums) // 2) - 1
            return (new_nums[index1] + new_nums[index2]) / 2
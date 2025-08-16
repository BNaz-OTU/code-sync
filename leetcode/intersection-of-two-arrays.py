class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        inter_set = set()

        for val in nums1:
            if ((val in nums1) and (val in nums2)):
                inter_set.add(val)
        
        return list(inter_set)
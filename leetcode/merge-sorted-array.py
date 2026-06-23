class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1 -> m
        # nums2 -> n

        combine = n + m - 1

        while n > 0 and m > 0:
            val1 = nums1[m - 1]
            val2 = nums2[n - 1]

            if (val1 < val2):
                nums1[combine] = val2
                n -= 1
            else:
                nums1[combine] = val1
                m -= 1
            
            combine -= 1
        
        while n > 0:
            nums1[combine] = nums2[n - 1]
            n -= 1
            combine -= 1
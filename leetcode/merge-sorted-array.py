class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # m -> nums1
        # n -> nums2

        combined = m + n - 1

        while m > 0 and n > 0:
            val1 = nums1[m - 1]
            val2 = nums2[n - 1]

            if (val2 > val1):
                nums1[combined] = val2
                n -= 1
            
            else:
                nums1[combined] = val1
                m -= 1
            
            combined -= 1
        
        while n > 0:
            nums1[combined] = nums2[n - 1]
            n -= 1
            combined -= 1
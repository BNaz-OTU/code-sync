class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        combine = m + n

        while n > 0 and m > 0:
            val1 = nums1[m - 1]
            val2 = nums2[n - 1]

            if (val2 >= val1):
                nums1[combine - 1] = val2
                n -= 1
            else:
                nums1[combine - 1] = val1
                m -= 1
            
            combine -= 1
        
        while n > 0:
            nums1[n - 1] = nums2[n - 1]
            n -= 1
        
        print(nums1)
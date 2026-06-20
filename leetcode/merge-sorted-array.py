class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # m -> nums1 | n -> nums2
        combine = m + n - 1

        while n > 0 and m > 0:
            if nums1[m - 1] <= nums2[n - 1]:
                nums1[combine] = nums2[n - 1]
                n -= 1
            else:
                nums1[combine] = nums1[m - 1]
                m -= 1
            
            combine -= 1
        
        print(f"n: {n}")
        print(f"m: {m}")

        while n > 0:
            nums1[combine] = nums2[n - 1]
            combine -= 1
            n -= 1
        
        # print(nums1)
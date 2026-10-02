class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # m -> nums1
        # n -> nums2

        combined = m + n - 1

        while (n - 1) >= 0 and (m - 1) >= 0:
            # print(nums1)
            if (nums1[m - 1] > nums2[n - 1]):
                nums1[combined] = nums1[m - 1]
                m -= 1
            
            elif (nums2[n - 1] >= nums1[m - 1]):
                nums1[combined] = nums2[n - 1]
                n -= 1
 
            combined -= 1
        
        # print(nums1[:m])
        # print(nums2[:n])

        while (n - 1) >= 0:
            nums1[combined] = nums2[n - 1]
            combined -= 1
            n -= 1
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict_nums1 = {}
        final = []

        for num in nums1:
            if (num in dict_nums1):
                dict_nums1[num] += 1
            else:
                dict_nums1[num] = 1
        
        for num in nums2:
            if (num in dict_nums1):
                dict_nums1[num] -= 1
                final.append(num)

                if (dict_nums1[num] == 0):
                    del dict_nums1[num]
        
        return final
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        final = [-1] * len(nums1)
        mono_stack = []

        nums1_dict_idx = {}

        for idx, val in enumerate(nums1):
            nums1_dict_idx[val] = idx

        for val in nums2:

            while (len(mono_stack) > 0 and val > mono_stack[-1]):
                index = nums1_dict_idx[mono_stack.pop()]
                final[index] = val
            
            if (val in nums1):
                mono_stack.append(val)
        
        return final
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        final = [-1] * len(nums1)
        mono_stack = []
        dict_idx = {}

        for idx, val in enumerate(nums1):
            dict_idx[val] = idx
        
        for val in nums2:
            
            while (len(mono_stack) > 0 and mono_stack[-1] < val):
                catch = mono_stack.pop()
                index = dict_idx[catch]
                final[index] = val
        
            if (val in dict_idx):
                mono_stack.append(val)
                
        return final
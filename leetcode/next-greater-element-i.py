class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        answer = [-1] * len(nums1)

        idx_dict = {}

        for idx in range(len(nums1)):
            idx_dict[nums1[idx]] = idx
        
        for val in nums2:
            while (len(stack) > 0 and stack[-1] < val):
                index = idx_dict[stack[-1]]
                answer[index] = val
                stack.pop()

            if (val in nums1):
                stack.append(val)
        
        return answer
            
        
        print(idx_dict)

        return answer
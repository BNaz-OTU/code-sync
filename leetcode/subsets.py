class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        final = []
        current = []

        def subset(idx, current):
            if (idx == len(nums)):
                final.append(current.copy())
                return
            
            current.append(nums[idx])
            subset(idx + 1, current)
            current.pop()
            subset(idx + 1, current)
        
        subset(0, current)
        return final
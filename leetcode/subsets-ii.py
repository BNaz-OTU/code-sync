class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        final = []
        current = []
        nums.sort()

        def subsetFinder(idx, current):
            if (idx == len(nums)):
                final.append(current.copy())
                return
            
            current.append(nums[idx])
            subsetFinder(idx + 1, current)
            current.pop()

            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1
            subsetFinder(idx + 1, current)
        
        subsetFinder(0, current)
        return final